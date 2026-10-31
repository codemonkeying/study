#!/usr/bin/env python3
"""
Offline CLI multiple-choice quiz - bank-agnostic, session-based.

A "session" is a subdir of banks/ holding a tests.md file, e.g.
    banks/linux/tests.md
    banks/aws/tests.md
    banks/windows-ad/tests.md
Drop a new banks/<name>/tests.md and it shows up automatically - no code change.

Per-session stats (right/wrong counters, a RECENT_N-slot shift register for weak-drill,
and a full ordered per-question attempt log 'history': [["YYYY-MM-DD HH:MM",
outcome], …] where outcome = 1 right / 0 wrong / "p" partial, scored as wrong)
live in  results/<session>@<device>.json  (one file per device, merged for display).

Bank format (per question):
    ## Test 1 - Title (N Q)
    1. Question text? (Select 2)
       - [ ] wrong  - **[x] correct**  - [ ] wrong
       - *why explanation shown after you answer*

Usage:
    study                      # menu: pick a session, then a test
    study mybank              # pick a test within mybank
    study mybank 3            # run mybank Test 3
    study mybank all          # pool ALL of mybank's questions into one run
    study mybank 3 shuffle    # shuffle question order (options always shuffle)
    study mybank weak         # re-drill only un-cleared weak spots
    study mybank new          # drill only NEW/unseen Qs (never answered / edited)
    study mybank all shuffle  # exam-sim: whole bank, shuffled
    study mybank history      # show past runs + weak spots
    study mybank practice_exam  # 90 Q, 90 min, domain-weighted, /900 (menu p)
    study set                  # list this host's settings (synced per-device)
    study set end_summary off  # e.g. hide the end-of-run WHY-review block
    study subnet               # subnetting practice drill (10 Qs, worked solutions)
    study subnet 20            # …20 questions
    study subnet history       # past drill scores + most-missed /n
    study subnet hard          # hard drill: all /n, wildcards, hosts->prefix
    study ref                  # print the subnetting table
    study ref mybank          # print a bank's quick ref (banks/<s>/ref.md)
    study sync                 # commit+push THIS device's records, pull others'
    study update               # pull the engine, then your data repo
    study --lint               # validate every bank (broken questions)

In-quiz slash commands:  /exit  /skip  /ref  /flag [N]  /sync  /help  (/sync, /help also at the menus)
"""
import glob
import hashlib
import json
import os
import random
import re
import socket
import subprocess
import sys
import tempfile
import time
import unicodedata
from datetime import datetime
import signal

try:  # closing the terminal = a normal pause, not a lost run
    signal.signal(signal.SIGHUP, lambda *_: (_ for _ in ()).throw(KeyboardInterrupt()))
except (AttributeError, ValueError):
    pass
try:
    # line editing for input(): arrow keys move the cursor instead of
    # printing ^[[D, plus Home/End, Ctrl+A/E, backspace mid-line
    import readline  # noqa: F401
except ImportError:
    pass

# ── paths / constants ───────────────────────────────────────────────────────
# realpath: works when run via a symlink (e.g. ~/.local/bin/study)
HERE = os.path.dirname(os.path.realpath(__file__))      # the engine (this repo)
CONF_FILE = os.path.join(os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config"),
                         "study", "config.toml")


def _data_dir():
    """Your data repo (banks + results): $STUDY_DATA, else config.toml data = "...",
    else ~/.local/share/study. Kept apart from the engine so updates never touch it."""
    if os.environ.get("STUDY_DATA"):
        return os.path.expanduser(os.environ["STUDY_DATA"])
    try:
        for line in open(CONF_FILE, encoding="utf-8"):
            m = re.match(r'\s*data\s*=\s*"([^"]+)"', line)
            if m:
                return os.path.expanduser(m.group(1))
    except OSError:
        pass
    return os.path.join(os.environ.get("XDG_DATA_HOME") or os.path.expanduser("~/.local/share"), "study")


def _conf(key, default):
    """A key = value line from config.toml (strings in quotes, true/false bare)."""
    try:
        for line in open(CONF_FILE, encoding="utf-8"):
            m = re.match(r'\s*' + key + r'\s*=\s*"?([^"#\n]*?)"?\s*(#.*)?$', line)
            if m:
                v = m.group(1).strip()
                return {"true": True, "false": False}.get(v.lower(), v)
    except OSError:
        pass
    return default


def _version():
    try:
        return open(os.path.join(HERE, "VERSION"), encoding="utf-8").read().strip()
    except OSError:
        return "?"


def _auto_update():
    """Once a day on launch: fast-forward the engine if upstream moved and the
    checkout is clean, then restart on the new code. Silent on any failure.
    Off with auto_update = false in config.toml or STUDY_NO_UPDATE=1."""
    if os.environ.get("STUDY_NO_UPDATE") or _conf("auto_update", True) is False:
        return
    stamp = os.path.join(os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache"),
                         "study", "last_update_check")
    try:
        if time.time() - os.path.getmtime(stamp) < 86400:
            return
    except OSError:
        pass
    try:
        os.makedirs(os.path.dirname(stamp), exist_ok=True)
        q = dict(cwd=HERE, capture_output=True, text=True, timeout=8)
        if subprocess.run(["git", "fetch", "-q"], **q).returncode:
            return
        open(stamp, "w").close()
        behind = subprocess.run(["git", "rev-list", "--count", "HEAD..@{u}"], **q).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "-uno"], **q).stdout.strip()
        if behind in ("", "0") or dirty:
            return
        old = _version()
        if subprocess.run(["git", "merge", "-q", "--ff-only", "@{u}"], **q).returncode:
            return
        print(f"{GRY}study updated {old} -> {_version()}{RST}", flush=True)
        os.environ["STUDY_NO_UPDATE"] = "1"
        os.execv(sys.executable, [sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    except Exception:
        return


DATA = _data_dir()
BANKS_DIR = os.path.join(DATA, "banks")          # your own/private banks (win on a name clash)
SHIPPED_BANKS = os.path.join(HERE, "banks")       # banks that ship with the engine
BANK_ROOTS = [BANKS_DIR] + ([SHIPPED_BANKS] if os.path.realpath(SHIPPED_BANKS) != os.path.realpath(BANKS_DIR) else [])


def bank_dir(session):
    """banks/<session> from the data repo if it has one, else the shipped copy."""
    for root in BANK_ROOTS:
        d = os.path.join(root, session)
        if os.path.isfile(os.path.join(d, "tests.md")) or os.path.isdir(os.path.join(d, "drafts")):
            return d
    return os.path.join(BANKS_DIR, session)
REF_SESSION = None      # bank whose ref.md /ref prints during a quiz
RUN_QS = []             # [(test_num, q)] of the current run, for /flag N
RUN_POS = 0             # current question number (1-based) in the run
RESULTS_DIR = os.path.join(DATA, "results")

# This device's tag - each machine writes only its OWN results file
# (results/<session>@<device>.json) so git push/pull never conflicts.
# Display merges every device's file back into one unified view.
# Override with QUIZ_DEVICE=name if the hostname is ugly/duplicated.
DEVICE = re.sub(r"[^A-Za-z0-9_-]", "-",
                (os.environ.get("QUIZ_DEVICE") or socket.gethostname().split(".")[0]
                 or "device"))

LETTERS = "ABCDEFGHIJ"   # option labels; lint flags questions with more
DEFAULT_PASS = 75        # % when a bank sets no pass mark
DEFAULT_MASTERY = 90     # % for "mastered" (green)
RECENT_N = 3            # weak retires after this many correct in a row
MENU_RUNS = 7           # past full-run scores shown per test in the menu
TITLE_MAX = 30          # menu test titles cut to this many cells (…)
NEW_ID_RE = re.compile(r"^T\d+:[0-9a-f]{12}$")   # current qid format
# mock exams: bank -> question count, minutes, domain weights (% by the first
# char of each question's @obj tag), scaled pass mark (100-900 scale)
# mock exams: banks/<name>/exam.json, e.g.
#   {"n": 90, "mins": 90, "pass": 750, "pbq": 5, "weights": {"1": 12, "2": 22}}
# question count, minutes, scaled pass mark (100-900), PBQs first, and domain
# weights (% by the first char of each question's @obj tag). No file = no mock.
def _load_exams():
    out = {}
    for f in [f for r in reversed(BANK_ROOTS) for f in glob.glob(os.path.join(r, "*", "exam.json"))]:
        try:
            j = json.load(open(f, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(j, dict):
            out[os.path.basename(os.path.dirname(f))] = j
    return out


EXAMS = _load_exams()
MOCK = {b: c for b, c in EXAMS.items()
        if isinstance(c.get("n"), int) and isinstance(c.get("mins"), (int, float))
        and isinstance(c.get("pass"), int) and isinstance(c.get("weights"), dict) and c["weights"]
        and type(c.get("n")) is int and c["n"] > 0}
for _c in MOCK.values():
    _c.setdefault("pbq", 0)
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

# ANSI colours
GRN, YEL, RED, GRY, CYN, RST = (
    "\033[92m", "\033[93m", "\033[91m", "\033[90m", "\033[96m", "\033[0m")


# ── per-host settings (synced) ──────────────────────────────────────────────
# Each machine has results/settings@<device>.json - tracked in git like the
# results files, so it syncs. A host reads only its OWN settings; defaults
# below fill any gaps. Change one with:  study set <key> <value>
SETTINGS_PATH = os.path.join(RESULTS_DIR, f"settings@{DEVICE}.json")
DEFAULT_SETTINGS = {
    # Show the end-of-run "── WHY you missed these ──" review block.
    # The explanations already appear inline as you answer, so this is optional.
    "end_summary": True,
}


def load_config():
    """This host's settings merged over DEFAULT_SETTINGS (bad file = defaults)."""
    cfg = dict(DEFAULT_SETTINGS)
    try:
        with open(SETTINGS_PATH, encoding="utf-8") as f:
            user = json.load(f)
        if isinstance(user, dict):
            cfg.update(user)
    except (ValueError, OSError):
        pass
    return cfg


def save_config(cfg):
    """Write this host's settings file atomically."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    _atomic_write_json(SETTINGS_PATH, cfg)


CONFIG = load_config()


# ── sessions / banks ────────────────────────────────────────────────────────
def list_sessions():
    """Sorted session names: every banks/<name>/tests.md that exists."""
    out = set()
    for root in BANK_ROOTS:
        try:
            for name in os.listdir(root):
                if os.path.isfile(os.path.join(root, name, "tests.md")):
                    out.add(name)
        except OSError:
            pass
    return sorted(out)


def bank_path(session):
    """Path to a session's question bank: banks/<session>/tests.md."""
    return os.path.join(bank_dir(session), "tests.md")


def results_path(session, device=None):
    """This device's own results file: results/<session>@<device>.json."""
    return os.path.join(RESULTS_DIR, f"{session}@{device or DEVICE}.json")


def device_files(session):
    """Every device's results file for this session, plus a legacy
    results/<session>.json if one exists (pre per-device layout)."""
    out = []
    legacy = os.path.join(RESULTS_DIR, f"{session}.json")
    if os.path.exists(legacy):
        out.append(legacy)
    try:
        for name in sorted(os.listdir(RESULTS_DIR)):
            if name.startswith(f"{session}@") and name.endswith(".json"):
                out.append(os.path.join(RESULTS_DIR, name))
    except OSError:
        pass
    return out


def parse_bank(path, keep_empty=False):
    """Return {test_num: {"title", "questions", "passmark", "mastery"}}.

    Thresholds: session defaults via top-of-file comments
        <!-- passmark: 80 -->   <!-- mastery: 95 -->
    per-test overrides on the '## Test N - Title' line
        <!-- pass: 90 -->       <!-- master: 98 -->
    Fallbacks: DEFAULT_PASS / DEFAULT_MASTERY.
    keep_empty=True keeps option-less questions (lint uses it to flag them).
    """
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    tests = {}
    cur_test = None
    cur_q = None

    session_pass = DEFAULT_PASS
    session_mastery = DEFAULT_MASTERY
    pass_default_re = re.compile(r"<!--\s*passmark:\s*(\d+)\s*-->", re.I)
    mastery_default_re = re.compile(r"<!--\s*mastery:\s*(\d+)\s*-->", re.I)
    pass_test_re = re.compile(r"<!--\s*pass:\s*(\d+)\s*-->", re.I)
    mastery_test_re = re.compile(r"<!--\s*master:\s*(\d+)\s*-->", re.I)
    test_re = re.compile(r"^##\s+Test\s+(\d+)\s*-\s*(.*)$", re.I)
    q_re = re.compile(r"^(\d+)\.\s+(.*)$")
    opt_re = re.compile(r"\[([ xX])\]\s*(.+?)\s*(?=-\s*\[|$)")
    note_re = re.compile(r"^\s*-?\s*\*(.+)\*\s*$")
    typed_re = re.compile(r"^\s*-\s*\[=\]\s*(.+?)\s*$")
    # multi-part PBQ part:  - [p] prompt :: A opt · B opt = answer | alt
    part_re = re.compile(r"^\s*-\s*\[p\]\s*(.+?)\s*$")
    # objective tag + optional source id of the old question it replaces:
    #   - @1.4.ports ~5.3
    obj_re = re.compile(r"^\s*-\s*@(\S+)(?:\s+~(\S+))?\s*$")

    def parse_opts(text):
        """[(option_text, is_correct)] from one line of '- [ ] / - [x]' items."""
        clean = text.replace("*", "")
        return [(t.strip(), m.lower() == "x")
                for m, t in opt_re.findall(clean) if t.strip()]

    def flush_q():
        """Close the current question and append it to its test."""
        nonlocal cur_q
        if cur_test is not None and cur_q and (cur_q["options"] or keep_empty):
            tests[cur_test]["questions"].append(cur_q)
        cur_q = None

    for line in lines:
        # session-default thresholds (only before any test starts)
        if cur_test is None:
            pd = pass_default_re.search(line)
            if pd:
                session_pass = int(pd.group(1))
            md = mastery_default_re.search(line)
            if md:
                session_mastery = int(md.group(1))

        m = test_re.match(line)
        if m:
            flush_q()
            n = int(m.group(1))
            title = m.group(2).strip()
            if "not yet captured" in title.lower():
                cur_test = None
                continue
            # per-test overrides, then strip the comments out of the title
            po = pass_test_re.search(title)
            mo = mastery_test_re.search(title)
            passmark = int(po.group(1)) if po else None
            mastery = int(mo.group(1)) if mo else None
            title = mastery_test_re.sub("", pass_test_re.sub("", title)).strip()
            # drop a trailing "(N Q)" count - the menu appends the real count
            title = re.sub(r"\s*\(\d+\s*Q\)\s*$", "", title, flags=re.I).strip()
            cur_test = n
            tests[n] = {"title": title, "questions": [],
                        "_passmark": passmark, "_mastery": mastery}
            continue

        if cur_test is None:
            continue

        # a '### ...' section (e.g. "### Test N key facts") ends the last
        # question so its trailing bullets don't get slurped as its note
        if line.lstrip().startswith("#"):
            flush_q()
            continue

        nm = note_re.match(line)
        if nm and cur_q is not None and "[" not in line:
            cur_q["note"] = nm.group(1).strip()
            continue

        m = q_re.match(line.strip())
        if m and not line.strip().startswith("- "):
            flush_q()
            q = m.group(2).strip()
            multi = "select" in q.lower()
            cur_q = {"q": q, "options": [], "note": "", "multi": multi}
            cur_q["options"].extend(parse_opts(line))
            continue

        om = obj_re.match(line)
        if om and cur_q is not None:
            cur_q["obj"] = om.group(1)
            if om.group(2):
                cur_q["src"] = om.group(2)
            continue

        pm = part_re.match(line)
        if pm and cur_q is not None:
            prompt, _, ans = pm.group(1).rpartition(" = ")
            prompt, _, opts = prompt.partition(" :: ")
            alts = [a.strip().strip("`") for a in ans.split(" | ") if a.strip()]
            cur_q.setdefault("parts", []).append(
                {"prompt": prompt.strip(), "opts": opts.strip(), "alts": alts})
            cur_q["options"] = [("pbq", True)]
            continue

        tm = typed_re.match(line)
        if tm and cur_q is not None:
            alts = [a.strip().strip("`") for a in tm.group(1).split(" | ") if a.strip()]
            cur_q["typed"] = alts
            cur_q["options"] = [(alts[0], True)]
            continue

        if cur_q is not None and "[" in line:
            cur_q["options"].extend(parse_opts(line))

    flush_q()
    # resolve each test's effective thresholds (override -> session default)
    for t in tests.values():
        t["passmark"] = t.pop("_passmark") or session_pass
        t["mastery"] = t.pop("_mastery") or session_mastery
    return tests


# ── stats (per session) ─────────────────────────────────────────────────────
_BANKS = {}   # session -> parsed bank cache


def qid(test_num, q):
    """Stable id for a question: test + short hash of the FULL normalised text
    (the old 40-char prefix let two Qs with the same opening share stats)."""
    norm = " ".join(q["q"].lower().split())
    return f"T{test_num}:{hashlib.sha1(norm.encode()).hexdigest()[:12]}"


def _bank(session):
    """Cached parse of a session's bank ({} if missing)."""
    if session not in _BANKS:
        try:
            _BANKS[session] = parse_bank(bank_path(session))
        except OSError:
            _BANKS[session] = {}
    return _BANKS[session]


def bank_ids(session):
    """Set of qids for questions CURRENTLY in the bank."""
    return {qid(n, q) for n, t in _bank(session).items() for q in t["questions"]}


def _legacy_map(session):
    """old id (test + first 40 chars) -> [(test_num, question)] in the bank."""
    mp = {}
    for n, t in _bank(session).items():
        for q in t["questions"]:
            mp.setdefault(f"T{n}:{q['q'][:40]}", []).append((n, q))
    return mp


def _rebuild_recent(st):
    """RECENT_N-slot register from the tail of history (full-correct = 1)."""
    if st.get("history"):
        st["recent"] = [1 if o == 1 else 0 for _, o in st["history"][-RECENT_N:]]


def _merge_stat(dst, src):
    """Fold src stats into dst (dst = newer data wins the register)."""
    for k in ("seen", "right", "wrong"):
        dst[k] = dst.get(k, 0) + src.get(k, 0)
    dst["history"] = sorted(dst.get("history", []) + src.get("history", []),
                            key=lambda h: h[0])
    dst["recent"] = (dst.get("recent") or src.get("recent") or [])[-RECENT_N:]
    _rebuild_recent(dst)
    dst.setdefault("q", src.get("q", ""))


def _split_shared(data, n, targets, st, title):
    """Several Qs shared ONE legacy id (same 40-char opening). Rebuild each
    Q's own stats from the run log: every full run of test n answered each
    of them once; the run's 'missed' list says which were wrong.
    Returns {qid: stats}, or None if the log doesn't account for `st`."""
    runs = [r for r in data.get("runs", []) if r.get("title") == title]
    out = {}
    for tn, q in targets:
        s = {"seen": 0, "right": 0, "wrong": 0, "recent": [], "history": [],
             "q": q["q"]}
        for r in runs:
            ok = q["q"][:60] not in r.get("missed", [])
            s["seen"] += 1
            s["right" if ok else "wrong"] += 1
            s["recent"] = (s["recent"] + [1 if ok else 0])[-RECENT_N:]
            s["history"].append([r["ts"][:16].replace("T", " "), 1 if ok else 0])
        out[qid(tn, q)] = s
    tot = {k: sum(s[k] for s in out.values()) for k in ("seen", "right", "wrong")}
    if tot != {k: st.get(k, 0) for k in ("seen", "right", "wrong")}:
        return None
    return out


def migrate_ids(session, data):
    """Re-key legacy 40-char-prefix ids to full-text hash ids, in place.
    Shared legacy ids are SPLIT per question from the run log (never cloned).
    Keys that match nothing in the bank move to data['orphans'] once, so they
    stop being rescanned and never count in stats. Returns True if changed."""
    qs = data.get("questions", {})
    legacy = [k for k in qs if not NEW_ID_RE.match(k)]
    if not legacy:
        return False
    mp = _legacy_map(session)
    tests = _bank(session)
    orphans = data.setdefault("orphans", {})
    for old in legacy:
        st = qs.pop(old)
        targets = mp.get(old)
        if not targets:
            orphans[old] = st  # reworded/removed question
            continue
        if len(targets) == 1:
            parts = {qid(*targets[0]): st}
        else:
            n = targets[0][0]
            parts = _split_shared(data, n, targets, st, tests[n]["title"])
            if parts is None:  # can't reconstruct: give it to the Q whose
                exact = [t for t in targets if t[1]["q"] == st.get("q")]  # text was
                parts = {qid(*(exact or targets)[0]): st}                 # recorded
        for new, s in parts.items():
            if new in qs:
                _merge_stat(qs[new], s)
            else:
                qs[new] = s
    return True


class CorruptResults(Exception):
    """A results file exists but can't be trusted (bad JSON / not a dict)."""


def _read_json(path):
    """None if missing. Raises CorruptResults if the file EXISTS but is
    unreadable/unparseable/not a results object, so a bad file is never
    mistaken for 'no history' and overwritten."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except ValueError as e:  # JSONDecodeError + UnicodeDecodeError
        raise CorruptResults(f"{path}: {e}")
    if not isinstance(data, dict):
        raise CorruptResults(f"{path}: not a results object")
    return data


def _atomic_write_json(path, data):
    """Write to a unique temp file, fsync, rename over, fsync the dir - a
    Ctrl-C/crash mid-write leaves the old file intact."""
    d = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp-", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise
    try:
        dfd = os.open(d, os.O_RDONLY)
        try:
            os.fsync(dfd)
        finally:
            os.close(dfd)
    except OSError:
        pass


def load_own(session):
    """Only THIS device's file - what run() mutates and saves back.
    Never load the merged blob here or stats double-count after a sync.
    A corrupt OWN file aborts (saving over it would wipe history)."""
    path = results_path(session)
    try:
        data = _read_json(path) or {}
    except CorruptResults as e:
        sys.exit(f"{RED}corrupt results file {e}\nNot touching it. "
                 f"Restore with: git checkout -- {os.path.relpath(path, DATA)}{RST}")
    data.setdefault("runs", [])
    data.setdefault("questions", {})
    data.setdefault("tests", {})
    migrate_ids(session, data)  # persisted on next save
    return data


def load_results(session):
    """Unified read across ALL devices (own + synced peers) for display.
    Counters sum; history concatenates + sorts by timestamp; the RECENT_N-slot
    'recent' register is REBUILT from the merged history's last RECENT_N outcomes
    (not file mtime, which git pull rewrites). A corrupt PEER file (half
    pull, conflict markers) is warned about and skipped, never fatal."""
    files = device_files(session)
    merged = {"runs": [], "questions": {}, "tests": {}}
    fallback_ts = {}
    own = os.path.abspath(results_path(session))
    for p in files:
        try:
            d = _read_json(p)
        except CorruptResults as e:
            if os.path.abspath(p) == own:
                load_own(session)  # aborts with restore instructions
            print(f"{YEL}warning: skipping unreadable peer file {e}{RST}",
                  file=sys.stderr)
            continue
        if not isinstance(d, dict):
            continue
        migrate_ids(session, d)  # in-memory only; peers' files untouched
        merged["runs"].extend(d.get("runs", []))
        newest = max((r.get("ts", "") for r in d.get("runs", [])), default="")
        for qidk, st in d.get("questions", {}).items():
            m = merged["questions"].setdefault(
                qidk, {"seen": 0, "right": 0, "wrong": 0, "recent": [],
                       "history": [], "q": st.get("q", "")})
            m["seen"] += st.get("seen", 0)
            m["right"] += st.get("right", 0)
            m["wrong"] += st.get("wrong", 0)
            m["history"].extend(st.get("history", []))
            # no-history legacy entries: register from the device that
            # practised most recently (by run timestamp, not file order)
            if st.get("recent") and newest >= fallback_ts.get(qidk, ""):
                m["_recent_fallback"] = st["recent"]
                fallback_ts[qidk] = newest
            if st.get("q"):
                m["q"] = st["q"]
        for tnum, ts in d.get("tests", {}).items():
            m = merged["tests"].setdefault(tnum, {})
            if ts.get("last"):
                m["last"] = max(ts["last"], m.get("last", ""))
    merged["runs"].sort(key=lambda r: r.get("ts", ""))
    for m in merged["questions"].values():
        m["history"].sort(key=lambda h: h[0])  # chronological across devices
        fb = m.pop("_recent_fallback", [])
        if m["history"]:
            m["recent"] = [1 if o == 1 else 0 for _, o in m["history"][-RECENT_N:]]
        else:  # legacy entries with no history log
            m["recent"] = fb[-RECENT_N:]
    return merged


def save_results(session, data):
    """Write only this device's own file (atomically)."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    _atomic_write_json(results_path(session), data)


def is_weak(st):
    """Weak = ever missed AND last RECENT_N outcomes not all fully-correct.
    'recent' is a RECENT_N-slot shift register (1=fully correct, 0=wrong/
    partial): RECENT_N in a row retires it; a later miss re-arms it."""
    return st.get("wrong", 0) > 0 and st.get("recent", [])[-RECENT_N:] != [1] * RECENT_N




def fmt_date(iso):
    """'2026-01-28' -> '28jan26'."""
    if not iso:
        return None
    try:
        day = datetime.strptime(iso.replace("T", " ").split()[0], "%Y-%m-%d")
        return day.strftime("%d%b%y").lower()
    except (ValueError, IndexError):
        return None


def score_cell(avg, passmark, mastery=DEFAULT_MASTERY):
    """Colour a rolling avg: <pass red, pass..<mastery orange, >=mastery green."""
    if avg is None:
        return f"{GRY}  - {RST}"
    if avg >= mastery:
        col = GRN
    elif avg >= passmark:
        col = YEL   # orange-ish
    else:
        col = RED
    return f"{col}{avg:>3d}%{RST}"


# ── lint ────────────────────────────────────────────────────────────────────
def lint():
    """Validate every bank's structure; return 1 if any blocking problem."""
    sessions = list_sessions()
    if not sessions:
        print(f"{RED}No banks found under {BANKS_DIR}{RST}")
        return 1
    problems = 0
    for s in sessions:
        tests = parse_bank(bank_path(s), keep_empty=True)
        print(f"\n{CYN}{s}{RST}  ({len(tests)} tests)")
        if not tests:
            print(f"  {RED}✗ no tests parsed{RST}")
            problems += 1
            continue
        for n in sorted(tests):
            t = tests[n]
            qs = t["questions"]
            issues = []
            seen_ids = {}
            for i, q in enumerate(qs, 1):
                ncorrect = sum(1 for _, c in q["options"] if c)
                if q.get("parts"):
                    for j, pt in enumerate(q["parts"], 1):
                        if not pt["alts"] or not pt["prompt"]:
                            issues.append(f"Q{i}: part {j} missing prompt or '= answer'")
                        elif pt["opts"] and not all(
                                re.fullmatch(r"[a-j]+", a.lower()) for a in pt["alts"]):
                            issues.append(f"Q{i}: part {j} has options but a non-letter answer")
                elif q.get("typed"):
                    pass
                elif not q["options"]:
                    issues.append(f"Q{i}: no options")
                elif ncorrect == 0:
                    issues.append(f"Q{i}: no correct answer marked")
                elif len(q["options"]) < 2:
                    issues.append(f"Q{i}: <2 options")
                if not q.get("typed") and len(q["options"]) > len(LETTERS):
                    issues.append(f"Q{i}: too many options (max {len(LETTERS)})")
                k = qid(n, q)
                if k in seen_ids:
                    issues.append(f"Q{i}: duplicate question text (same as Q{seen_ids[k]})")
                seen_ids.setdefault(k, i)
                if not q["note"]:
                    issues.append(f"Q{i}: no *why* note")
            status = f"{GRN}ok{RST}" if not issues else f"{RED}{len(issues)} issue(s){RST}"
            print(f"  Test {n:<2} {len(qs):>2} Q  {status}")
            for msg in issues:
                sev = RED if any(w in msg for w in ("no correct", "no options", "part ",
                                                    "too many", "duplicate")) else YEL
                print(f"       {sev}- {msg}{RST}")
                if sev == RED:
                    problems += 1
    if problems:
        print(f"\n{RED}✗ {problems} blocking problem(s){RST}")
    else:
        print(f"\n{GRN}✓ all banks valid{RST}")
    return 1 if problems else 0


# ── quiz run ────────────────────────────────────────────────────────────────
RESUME_PATH = os.path.join(RESULTS_DIR, f"resume@{DEVICE}.json")


def _resume_own():
    try:
        d = _read_json(RESUME_PATH)
    except CorruptResults as e:
        print(f"{YEL}⚠ paused-run file unreadable, starting it fresh: {e}{RST}")
        d = None
    if not isinstance(d, dict):
        d = {}
    d.setdefault("active", {})
    d.setdefault("consumed", [])
    return d


def _resume_all():
    """Paused runs from EVERY device (synced), minus any a device has consumed.
    Returns {key: state}, newest state per key."""
    files = glob.glob(os.path.join(RESULTS_DIR, "resume@*.json"))
    docs = []
    for f in files:
        try:
            d = _read_json(f)
        except CorruptResults as e:
            print(f"{YEL}⚠ skipping unreadable paused-run file: {e}{RST}")
            continue
        if isinstance(d, dict):
            docs.append(d)
    gone = {u for d in docs for u in d.get("consumed", [])}
    out = {}
    for d in docs:
        for k, st in d.get("active", {}).items():
            if st.get("uid") in gone:
                continue
            if k not in out or st.get("ts", "") > out[k].get("ts", ""):
                out[k] = st
    return out


def _resume_consume(key, uid):
    d = _resume_own()
    d["active"].pop(key, None)
    if uid and uid not in d["consumed"]:
        d["consumed"] = (d["consumed"] + [uid])[-300:]
    os.makedirs(RESULTS_DIR, exist_ok=True)
    _atomic_write_json(RESUME_PATH, d)


def _resume_put(key, state):
    d = _resume_own()
    d["active"][key] = state
    os.makedirs(RESULTS_DIR, exist_ok=True)
    _atomic_write_json(RESUME_PATH, d)


def _jsonable(x):
    if isinstance(x, (set, frozenset)):
        return sorted(x)
    if isinstance(x, (list, tuple)):
        return [_jsonable(v) for v in x]
    if isinstance(x, dict):
        return {k: _jsonable(v) for k, v in x.items()}
    return x


def run_key(session, test_num_of, weak_only, unseen_only, mock):
    if mock:
        base = "mock"
    elif test_num_of:
        base = f"T{test_num_of}"
    else:
        base = "all"
    flags = "".join(f"+{n}" for n, on in (("weak", weak_only), ("new", unseen_only)) if on)
    return f"{session}:{base}{flags}"


def _fmt_secs(t):
    t = int(t)
    h, m, sec = t // 3600, t % 3600 // 60, t % 60
    return f"{h}h {m:02d}m {sec:02d}s" if h else f"{m}m {sec:02d}s"


Q_CAP = 300   # max secs one question can add to the run timer


def _flag_cmd(low):
    """/flag or /flag N inside a quiz. True if it was a /flag command."""
    m = re.fullmatch(r"/f(?:lag)?\s*(\d*)", low)
    if not m:
        return False
    n = m.group(1)
    if not n:
        n = input(f"  {YEL}Which question number to flag? "
                  f"(Enter = this one, Q{RUN_POS}) {RST}").strip() or str(RUN_POS)
    if not n.isdigit() or not 1 <= int(n) <= min(RUN_POS, len(RUN_QS)):
        print(f"  {YEL}pick a question you've seen: 1–{RUN_POS}{RST}")
        return True
    why = input(f"  {YEL}What's weird? (optional, Enter to skip) {RST}").strip()
    tn, q = RUN_QS[int(n) - 1]
    path = os.path.join(RESULTS_DIR, f"flags@{DEVICE}.json")
    d = _read_json(path) if os.path.exists(path) else {}
    d.setdefault("flags", []).append({"ts": datetime.now().isoformat(timespec="seconds"), "bank": REF_SESSION,
              "test": tn, "id": qid(tn, q), "q": q["q"][:200], "why": why,
              "fixed": False})
    os.makedirs(RESULTS_DIR, exist_ok=True)
    _atomic_write_json(path, d)
    print(f"  {GRN}⚑ flagged Q{n} (Test {tn}) - 'study flags' lists them{RST}")
    return True


def cmd_flags():
    """List open flagged questions from every device."""
    out = []
    for f in sorted(glob.glob(os.path.join(RESULTS_DIR, "flags@*.json"))):
        d = _read_json(f)
        dev = os.path.basename(f)[6:-5]
        for e in d.get("flags", []):
            if not e.get("fixed"):
                out.append((e.get("ts", ""), dev, e))
    if not out:
        print(f"{GRN}No open flags.{RST}")
        return 0
    for ts, dev, e in sorted(out, key=lambda x: x[0]):
        print(f"{YEL}⚑{RST} {ts[:16]} {GRY}{dev}{RST}  {e.get('bank')} T{e.get('test')}  "
              f"{e.get('q', '')[:90]}")
        if e.get("why"):
            print(f"     {CYN}› {e['why']}{RST}")
    print(f"{GRY}{len(out)} open flag(s){RST}")
    return 0


class Quit(Exception):
    """Raised by ask() on /exit - ends a run but still saves it."""


def show_stem(stem):
    """A stem may embed command output: '¶' = newline, shown as an
    indented block (grey) so ipconfig/show output reads like a terminal."""
    if "¶" not in stem:
        return stem
    head, *body = stem.split("¶")
    # an inline option list 'A foo · B bar · C baz' -> one option per line
    out = []
    for ln in body:
        if LETTER_OPTS_RE.match(ln):
            out += [f"  {L}) {t}" for L, t in
                    re.findall(r"([A-J]) (.+?)(?= · [A-J] |$)", ln.strip())]
        else:
            out.append(ln)
    block = "\n".join(f"      {ln.rstrip()}" for ln in out)
    return f"{head.rstrip()}\n{block}"


# IOS shorthand the exam/IOS accept interchangeably; typed answers compare
# after expansion, so 'int gi0/20; shut' == 'interface g0/20; shutdown'
IOS_HEADS = {"interface", "int", "shutdown", "shut", "no", "access-list",
             "copy", "write", "wr", "line", "ip", "switchport", "show", "sh",
             "hostname", "enable", "username", "vlan", "router", "network",
             "spanning-tree", "crypto", "logging", "snmp-server", "ntp",
             "transport", "channel-group", "description", "service",
             "conf", "configure"}
IOS_WORDS = {"int": "interface", "shut": "shutdown", "sh": "show",
             "run": "running-config", "start": "startup-config",
             "conf": "configure", "t": "terminal", "wr": "write",
             "mem": "memory", "br": "brief", "https": "443", "http": "80",
             "ssh": "22", "telnet": "23", "www": "80", "domain": "53"}
IFACE_RE = re.compile(r"^(gigabitethernet|gig|gi|g|fastethernet|fa|f|"
                      r"tengigabitethernet|te|ethernet|eth|e)(\d.*)$", re.I)
IFACE_FULL = {"g": "gigabitethernet", "f": "fastethernet", "t": "tengigabitethernet",
              "e": "ethernet"}


def ios_norm(toks):
    out = []
    for i, w in enumerate(toks):
        lw = w.lower()
        if lw == "vlan" and i + 1 < len(toks) and toks[i + 1].isdigit() and \
                i and toks[i - 1].lower() in ("interface", "int"):
            continue                    # 'interface vlan 30' == 'interface vlan30'
        if i and toks[i - 1].lower() == "vlan" and lw.isdigit() and \
                i > 1 and toks[i - 2].lower() in ("interface", "int"):
            out.append("vlan" + lw)
            continue
        m = IFACE_RE.match(lw)
        if m:
            out.append(IFACE_FULL[m.group(1)[0]] + m.group(2))
            continue
        if lw in ("https", "http", "ssh", "telnet", "www", "domain") and \
                not (i and toks[i - 1].lower() == "eq"):
            out.append(w)               # only port keywords after 'eq' map
            continue
        if lw == "t" and not (i and toks[i - 1].lower() in ("conf", "configure")):
            out.append(w)
            continue
        out.append(IOS_WORDS.get(lw, w))
    # 'host X' == 'X 0.0.0.0' in ACLs
    j = 0
    res = []
    while j < len(out):
        if out[j].lower() == "host" and j + 1 < len(out):
            res += [out[j + 1], "0.0.0.0"]
            j += 2
            continue
        res.append(out[j])
        j += 1
    # 'write' alone == 'write memory'
    res = [x for k, x in enumerate(res)]
    if res[:1] == ["write"] and (len(res) == 1 or res[1] == ";"):
        res.insert(1, "memory")
    return res


WIN_CMDS = {"ping", "tracert", "pathping", "ipconfig", "netstat", "nslookup", "arp",
            "route", "netsh", "nbtstat", "getmac", "gpupdate", "gpresult", "robocopy", "net"}


# Linux iproute2 accepts any unambiguous prefix: ip a / addr / address, ip n / neigh / neighbour,
# show = s = list = ls. Only applied after `ip` (or `sudo ip`), and only when the next
# word is a Linux object, so Cisco's `ip route 0.0.0.0 ...` and `ip helper-address` are untouched.
IP2_OBJ = {"a": "address", "ad": "address", "add": None, "addr": "address", "addre": "address",
           "addres": "address", "address": "address",
           "l": "link", "li": "link", "lin": "link", "link": "link",
           "n": "neighbour", "ne": "neighbour", "nei": "neighbour", "neigh": "neighbour",
           "neighbor": "neighbour", "neighbour": "neighbour",
           "r": "route", "ro": "route", "rou": "route", "rout": "route", "route": "route"}
IP2_VERB = {"s": "show", "sh": "show", "sho": "show", "show": "show", "list": "show",
            "ls": "show", "lst": "show", "a": "add", "ad": "add", "add": "add",
            "d": "delete", "del": "delete", "delete": "delete", "f": "flush", "flush": "flush"}


def linux_ip_norm(toks):
    lo = [t.lower() for t in toks]
    i = 1 if lo[:1] == ["sudo"] else 0
    if lo[i:i + 1] != ["ip"] or len(lo) < i + 2:
        return toks
    obj = IP2_OBJ.get(lo[i + 1])
    if not obj:
        return toks
    rest = toks[i + 2:]
    if obj == "route" and rest and re.match(r"\d", rest[0]):
        return toks          # Cisco: ip route 10.0.0.0 255.0.0.0 ...
    if rest and lo[i + 2] in IP2_VERB:
        rest = [IP2_VERB[lo[i + 2]]] + rest[1:]
    if not rest:
        rest = ["show"]      # bare `ip a` = `ip address show`
    return toks[:i] + ["ip", obj] + rest


BPF_KW = {"host", "net", "port", "portrange", "src", "dst", "ether", "proto", "gateway"}
BPF_OPS = {"&&": "and", "||": "or", "!": "not"}


def bpf_norm(toks):
    """tcpdump: a quoted filter == unquoted (quotes stripped, &&/||/! inside
    quotes -> and/or/not, since the shell can't see them there). Then glue each
    primitive into one unit ('host 10.0.0.9', 'src port 53') so order-free
    sorting can swap whole primitives but can't scramble 'host and X port Y'."""
    out, quoted = [], False
    for t in toks:
        if t[:1] in "'\"" or t[-1:] in "'\"":
            quoted = True
        t = t.strip("'\"")
        if t:
            out.append(t)
    if quoted:
        out = [BPF_OPS.get(t, t) for t in out]
    res, i = [], 0
    while i < len(out):
        t = out[i]
        if t.lower() in BPF_KW:
            unit = [t]
            while i + 1 < len(out) and out[i + 1].lower() in BPF_KW:
                i += 1
                unit.append(out[i])
            nxt = out[i + 1] if i + 1 < len(out) else ""
            if nxt and nxt.lower() not in ("and", "or", "not") and nxt[:1] != "-":
                i += 1
                unit.append(nxt)
            res.append(" ".join(unit))
        else:
            res.append(t)
        i += 1
    return res


def typed_ok(ans, alts):
    """Does a typed command match any accepted answer? Whitespace-collapsed;
    flag/argument ORDER doesn't matter (same tokens after the command).
    Case only matters if the accepted answer has capitals (nmap -O vs -o),
    so 'IPCONFIG /ALL' passes but 'nmap -sv' doesn't."""
    def norm(t):
        t = re.sub(r"\s*;\s*", " ; ", t.strip())
        if re.fullmatch(r"[\d\s,/.]+", t):          # number lists: commas = spaces
            t = t.replace(",", " ")
        toks = t.split()
        toks = linux_ip_norm(toks)
        if toks and toks[0].lower() == "tcpdump":
            toks = bpf_norm(toks)
        if toks and toks[0].lower() in IOS_HEADS:  # IOS: expand shorthand
            toks = ios_norm(toks)
        # bundled single-letter flags are order-free: -tulpn == -plunt
        toks = [("-" + "".join(sorted(x[1:]))) if re.fullmatch(r"-[a-zA-Z]{2,}", x)
                and not re.fullmatch(r"-(s[a-zA-Z]|nn|v2c|p-)", x) else x for x in toks]
        return toks
    a = norm(ans)
    for alt in alts:
        b = norm(alt)
        if any(c.isupper() for c in alt):
            x, y = a, b
        else:   # case-free, but -p and -P are different flags (ssh, nmap, scp)
            win = bool(b) and b[0].lower() in WIN_CMDS
            lo = lambda ts: [t if (t[:1] == "-" and not win and i) else t.lower()
                             for i, t in enumerate(ts)]
            x, y = lo(a), lo(b)
        # free argument order only for commands (first token has a letter),
        # so "128 64 32 ..." or an IP can't be answered in any order
        cmd = bool(y) and any(c.isalpha() for c in y[0]) and \
            any(t[:1] in "-/" for t in y[1:])
        if x == y or (cmd and x[:1] == y[:1] and sorted(x[1:]) == sorted(y[1:])):
            return True
        # answer is a bare flag ("-a", "/flushdns") and the user typed the whole
        # command ("netstat -a"): drop the one leading command word
        if len(y) == 1 and y[0][:1] in "-/" and len(x) == 2 and \
                x[0][:1] not in "-/" and x[1:] == y:
            return True
        # every token one char (3 1 4 2, b c a): spacing/commas optional.
        # "1 11" has a 2-char token, so "111" can never sneak through.
        if len(y) > 1 and all(len(t) == 1 for t in y) and \
                re.sub(r"[\s,]", "", "".join(x)) == "".join(y):
            return True
    return False


def format_problem(raw, alts, letters=None, letter_pbq=False):
    """Answer in the wrong FORMAT (digits for a letter question, letters for a
    number list, a letter that isn't an option)? Return a hint to re-prompt
    with instead of marking it wrong. None = format fine, go and mark it."""
    got = re.sub(r"[\s,]", "", raw)
    want = re.sub(r"[\s,]", "", alts[0]) if alts else ""
    if letters:                                   # options are shown
        bad = sorted({c for c in got.upper() if c not in letters})
        if bad:
            return (f"answer with the option letters {letters[0]}–{letters[-1]}"
                    f" - '{''.join(bad).lower()}' isn't one of them")
        return None
    if letter_pbq:                    # only real letter-order PBQs ('dig' is a command)
        if not got.isalpha():
            return "answer with letters (e.g. 'bca'), not numbers"
    elif alts and all(re.fullmatch(r"[\d\s,/.:]+", a) for a in alts) and re.search(r"[a-zA-Z]", got):
        return "this one wants numbers, not letters"
    return None


LETTER_ANS_RE = re.compile(r"^[a-h]{2,8}$")
LETTER_OPTS_RE = re.compile(r"^\s*A \S.* · B \S")


def relabel_letters(q):
    """Letter-matching PBQ ('Type the letters in order, e.g. abc' with an
    '¶  A foo · B bar · C baz' option list): return a copy with the options
    randomly re-lettered and the answer, alternatives and note remapped, so
    the letters can't be memorised. Any other question comes back unchanged."""
    ans = (q.get("typed") or [""])[0]
    if not LETTER_ANS_RE.match(ans):
        return q
    segs = q["q"].split("¶")
    idx = next((k for k in range(len(segs) - 1, -1, -1)
                if LETTER_OPTS_RE.match(segs[k])), None)
    if idx is None:
        return q
    items = re.findall(r"([A-H]) (.+?)(?= · [A-H] |$)", segs[idx].strip())
    labels = [L for L, _ in items]
    if len(labels) < 2 or not set(ans.upper()) <= set(labels):
        return q
    perm = labels[:]
    for _ in range(20):                         # avoid a trivial abc… answer
        random.shuffle(perm)
        new = "".join(perm[labels.index(c.upper())].lower() for c in ans)
        if new not in ("abcdefgh"[:len(new)], "abcdefgh"[:len(new)][::-1]):
            break
    to_new = dict(zip(labels, perm))
    text = dict(items)
    by_new = {to_new[L]: text[L] for L in labels}
    segs[idx] = "  " + " · ".join(f"{L} {by_new[L]}" for L in sorted(by_new))

    def fix_note(note):
        # remap "B load balancer"-style refs, only where the next word really
        # belongs to that option's text (so the article "A" is left alone)
        def sub(m):
            L, word = m.group(1), m.group(2)
            if L in text and word.lower().strip(".,;:()") in text[L].lower():
                return f"{to_new[L]} {word}"
            return m.group(0)
        return re.sub(r"(?<![A-Za-z])([A-H]) ([A-Za-z0-9][\w./+-]*)", sub, note)

    q2 = dict(q)
    q2["q"] = "¶".join(segs)
    q2["typed"] = [new, " ".join(new), ",".join(new)]
    q2["note"] = fix_note(q.get("note", ""))
    return q2


# the old inline "how to answer" sentence, removed from the stem because the
# new layout prints its own hint line: "Type the letters in order, e.g. abc."
LETTER_HINT_RE = re.compile(
    r"\s*Type the (?:class )?letters?\b(?:(?!¶).)*?(?:e\.g\.\s*[a-h ,]+\.|\.(?=\s|$))"
    r"(?:\s*A letter can be used twice\.)?"
    r"|\s*e\.g\.\s*[a-h ,]+\.(?:\s*A letter can be used twice\.)?",
    re.I)


def letter_pbq_view(q):
    """Pretty layout for a letter-matching PBQ: numbered items, one option
    per line, one hint line. Returns None if q isn't one."""
    ans = (q.get("typed") or [""])[0]
    if not LETTER_ANS_RE.match(ans):
        return None
    segs = q["q"].split("¶")
    oi = next((k for k in range(len(segs) - 1, -1, -1)
               if LETTER_OPTS_RE.match(segs[k])), None)
    if oi is None:
        return None
    opts = re.findall(r"([A-H]) (.+?)(?= · [A-H] |$)", segs[oi].strip())
    head = LETTER_HINT_RE.sub("", segs[0]).strip()
    reuse = "can be used twice" in q["q"] or len(set(ans)) < len(ans)
    lines = [head]
    items = []
    for sg in segs[1:oi] + segs[oi + 1:]:
        sg = LETTER_HINT_RE.sub("", sg).strip()
        if not sg:
            continue
        if sg.lower().startswith("slot "):          # "Slot 1 · job" lines
            items.append(re.sub(r"^slot\s*(\d+)\s*·\s*", "", sg, flags=re.I))
        elif " · " in sg and not items:
            body = re.sub(r"^[A-Za-z][\w -]{0,20}:\s+", "", sg)
            items += [x.strip() for x in body.split(" · ") if x.strip()]
        else:
            lines.append(sg)
    out = [lines[0]] + [f"   {ln}" for ln in lines[1:]]
    for k, it in enumerate(items, 1):
        out.append(f"   {CYN}{k}.{RST} {it}")
    out.append("")
    for L, text in opts:
        out.append(f"   {CYN}{L}){RST} {text}")
    if items:
        out.append(f"   {GRY}(type {len(items)} letters, one per numbered item, "
                   f"in order{'; a letter can repeat' if reuse else ''}){RST}")
    elif re.search(r"\(\d\)", q["q"]):          # diagram with numbered slots
        out.append(f"   {GRY}(type {len(ans)} letters, one per slot, in slot order"
                   f"{'; a letter can repeat' if reuse else ''}){RST}")
    else:
        out.append(f"   {GRY}(type all {len(ans)} letters in the right order){RST}")
    return "\n".join(out)


def ask_typed(q, idx, total):
    """Typed-command question. Returns (answer_text, skipped)."""
    view = letter_pbq_view(q)
    if view:
        print(f"Q{idx}/{total}. {view}")
    else:
        print(f"Q{idx}/{total}. {show_stem(q['q'])}")
        first = q["typed"][0]
        hint = "type the command" if re.match(r"[a-z]", first) and " " in first else "type the answer"
        print(f"   {GRY}({hint}){RST}")
    while True:
        raw = input(f"\001{CYN}\002$\001{RST}\002 ").strip()
        low = raw.lower()
        if low in ("/exit", "/quit", "/q"):
            raise Quit()
        if low in ("/skip", "/s"):
            return "", True
        if _flag_cmd(low):
            continue
        if low in ("/sync",):
            cmd_sync()
            continue
        if low in ("/ref", "/r"):
            print_ref(REF_SESSION, quiz=True)
            continue
        if low in ("/help", "/h", "/?"):
            print(f"  {GRY}type the full command · /skip · /ref · /flag · /sync · /exit{RST}")
            continue
        if raw:
            hint = format_problem(raw, q["typed"], letter_pbq=bool(view))
            if hint:
                print(f"  {YEL}{hint} - try again{RST}")
                continue
            return raw, False


def shuffle_part(pt):
    """Copy of a single-letter-answer PBQ part with its options in a random
    order and the answer letter remapped (bank letters would otherwise sit
    still and skew towards A). Multi-letter/typed parts come back unchanged."""
    items = re.findall(r"([A-J]) (.+?)(?= · [A-J] |$)", pt["opts"])
    labels = [L for L, _ in items]
    if len(items) < 2 or not all(re.fullmatch(r"[A-Ja-j]", a) for a in pt["alts"]) \
            or not all(a.upper() in labels for a in pt["alts"]):
        return pt
    order = [t for _, t in items]
    random.shuffle(order)
    old_text = dict(items)
    alts = [labels[order.index(old_text[a.upper()])].lower() for a in pt["alts"]]
    opts = " · ".join(f"{L} {t}" for L, t in zip(labels, order))
    return {**pt, "opts": opts, "alts": alts}


def part_answer(pt):
    """Display form of a part's answer: 'c) Fail-closed' for letter parts."""
    a = pt["alts"][0]
    if pt["opts"] and re.fullmatch(r"[A-Ja-j]", a):
        text = dict(re.findall(r"([A-J]) (.+?)(?= · [A-J] |$)", pt["opts"])).get(a.upper())
        if text:
            return f"{a.lower()}) {text}"
    return a


def ask_parts(q, idx, total):
    """Multi-part PBQ: show the scenario once, ask each part in turn.
    Returns ([(part, answer, ok)], skipped)."""
    print(f"Q{idx}/{total}. {show_stem(q['q'])}")
    n = len(q["parts"])
    print(f"   {GRY}({n} parts, each scored · /skip skips the rest){RST}")
    res = []
    for j, pt in enumerate(q["parts"], 1):
        if j > 1 and q["q"].count("¶") >= 3:   # diagram/table: re-show it
            print(f"\n   {GRY}{'─' * 50}{RST}")
            print(f"   {show_stem(q['q'])}")
        print(f"\n   {CYN}Part {j}/{n}.{RST} {pt['prompt']}")
        if pt["opts"]:
            pt = shuffle_part(pt)   # fresh option order each run
            for L, text in re.findall(r"([A-J]) (.+?)(?= · [A-J] |$)", pt["opts"]):
                print(f"      {L}) {text}")
        while True:
            raw = input(f"\001{CYN}\002$\001{RST}\002 ").strip()
            low = raw.lower()
            if low in ("/exit", "/quit", "/q"):
                raise Quit()
            if low in ("/skip", "/s"):
                res += [(p, "", False) for p in q["parts"][j - 1:]]
                return res, not any(ok for _, _, ok in res)
            if _flag_cmd(low):
                continue
            if low in ("/sync",):
                cmd_sync()
                continue
            if low in ("/ref", "/r"):
                print_ref(REF_SESSION, quiz=True)
                continue
            if low in ("/help", "/h", "/?"):
                print(f"  {GRY}answer this part · /skip · /ref · /flag · /sync · /exit{RST}")
                continue
            if raw:
                opt_letters = "".join(re.findall(r"(?:^|· )([A-J]) ", pt["opts"] or ""))
                hint = format_problem(raw, pt["alts"], opt_letters or None)
                if hint:
                    print(f"   {YEL}{hint} - try again{RST}")
                    continue
                break
        ok = typed_ok(raw, pt["alts"])
        print(f"   {GRN}✓{RST}" if ok else
              f"   {RED}✗{RST} answer: {GRN}{part_answer(pt)}{RST}")
        res.append((pt, raw, ok))
    return res, False


def ask(q, opts, n_correct, idx, total):
    """Show a question, return (picked_set, skipped)."""
    already = "select" in q["q"].lower()
    tag = "" if already else (f" (Select {n_correct})"
                              if q["multi"] or n_correct > 1 else "")
    print(f"Q{idx}/{total}. {show_stem(q['q'])}{tag}")
    for j, (text, _) in enumerate(opts):
        print(f"   {LETTERS[j]}) {text}")
    valid = LETTERS[:len(opts)]
    while True:
        raw = input("> ").strip()
        low = raw.lower()
        if low in ("/exit", "/quit", "/q"):
            raise Quit()
        if low in ("/skip", "/s"):
            return set(), True
        if _flag_cmd(low):
            continue
        if low in ("/sync",):
            cmd_sync()
            continue
        if low in ("/ref", "/r"):
            print_ref(REF_SESSION, quiz=True)
            continue
        if low in ("/help", "/h", "/?"):
            print(f"  {GRY}letters e.g. 'ac' to answer · /skip · /ref · /flag · /sync · /exit · /help{RST}")
            continue
        # answer must be ONLY option letters (spaces/commas ok) - blank,
        # typos or out-of-range letters re-prompt instead of scoring a miss
        letters = re.sub(r"[\s,]", "", raw.upper())
        if letters and all(c in valid for c in letters):
            if len(set(letters)) != n_correct:
                print(f"  {YEL}pick {n_correct} - you gave {len(set(letters))}. "
                      f"Try again, or /skip{RST}")
                continue
            return set(letters), False
        bad = sorted({c for c in letters if c not in valid})
        why = f"'{''.join(bad).lower()}' isn't an option - " if bad else ""
        print(f"  {YEL}{why}answer with letters {valid[0]}–{valid[-1]} (e.g. 'ac'), "
              f"or /skip /exit{RST}")


def _ask_mc(q, i, total, shuffle, missed, done, score):
    """Multiple-choice question. Returns (got_full, partial, done, score);
    got_full None = skipped."""
    opts = list(q["options"])
    # ALWAYS shuffle options (banks are written answer-first, so fixed order
    # leaks the answer as A / ABC). True/False keeps its order; "all/none of
    # the above"-style options stay pinned last. `shuffle` mode now only
    # affects question order.
    if sorted(o[0].strip().lower() for o in opts) != ["false", "true"]:
        pin = [o for o in opts if re.search(r"\bof the above\b|^any of these|^none of these", o[0], re.I)]
        rest = [o for o in opts if o not in pin]
        random.shuffle(rest)
        opts = rest + pin
    correct = {LETTERS[j] for j, (_, c) in enumerate(opts) if c}
    n_correct = len(correct)
    # 'B EIGRP · E OSPF': letter AND text, so the miss line shows the answer itself
    ans_txt = " · ".join(f"{LETTERS[j]} {t}" for j, (t, c) in enumerate(opts) if c)
    picked, skipped = ask(q, opts, n_correct, i, total)
    if skipped:
        print(f"  {GRY}skipped - correct: {ans_txt}{RST}")
        if q["note"]:
            print(f"  {GRY}› {expand_note(q['note'])}{RST}")
        print()
        return None, False, done, score
    done += 1
    # scoring is ALL-OR-NOTHING (like the real exam): a partial
    # multi-select earns 0 everywhere; "p" is kept only as a label
    got_full = picked == correct
    partial = bool(not got_full and picked and picked.issubset(correct))
    if got_full:
        score += 1
        print(f"  {GRN}✓ correct{RST}")
    elif partial:
        print(f"  {YEL}~ partial ({len(picked)}/{n_correct}) - scores 0 "
              f"(exam is all-or-nothing){RST}  correct: {GRN}{ans_txt}{RST}")
        missed.append({"q": q, "opts": opts, "correct": correct, "picked": picked})
    else:
        print(f"  {RED}✗ wrong{RST}  correct: {GRN}{ans_txt}{RST}")
        missed.append({"q": q, "opts": opts, "correct": correct, "picked": picked})
    return got_full, partial, done, score


def _record(qstats, tn, q, got_full, partial):
    """Update one question's stats (persisted by the caller)."""
    st = qstats.setdefault(qid(tn, q),
                           {"seen": 0, "right": 0, "wrong": 0,
                            "recent": [], "history": [], "q": q["q"]})
    st["seen"] += 1
    if got_full:
        st["right"] = st.get("right", 0) + 1
    else:
        st["wrong"] += 1
    recent = st.setdefault("recent", [])
    recent.append(1 if got_full else 0)
    del recent[:-RECENT_N]
    # full ordered attempt log (never truncated): [datetime, outcome]
    # outcome: 1=correct, 0=wrong, "p"=partial (scored as wrong)
    outcome = 1 if got_full else ("p" if partial else 0)
    st.setdefault("history", []).append(
        [datetime.now().strftime("%Y-%m-%d %H:%M"), outcome])


def run(session, qs, test_num_of, title, shuffle=False, weak_only=False,
        unseen_only=False, mock=None):
    """qs: list of (test_num, question). test_num_of = the single test being
    run (None for pooled all/weak/new runs); only used for the title."""
    global REF_SESSION
    REF_SESSION = session
    data = load_own(session)       # mutate + save only THIS device's file
    qstats = data["questions"]
    key = run_key(session, test_num_of, weak_only, unseen_only, mock)
    saved = _resume_all().get(key)
    resumed = None
    if saved:
        where = saved.get("pos", 0) + 1
        try:
          ans = input(f"{YEL}⏸ {title}: paused at Q{where}/{saved.get('total', '?')} "
                    f"({saved.get('score', 0):.0f}/{saved.get('done', 0)} so far, "
                    f"{_fmt_secs(saved.get('elapsed', 0))} used"
                    f"{', from ' + saved['device'] if saved.get('device') not in (None, DEVICE) else ''}"
                    f"). Resume? [Y/n] {RST}").strip().lower()
          while ans not in ("", "y", "yes", "n", "no"):
            ans = input(f"{YEL}  y = resume, n = discard and start fresh: {RST}").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{GRY}Left paused - nothing changed.{RST}")
            return False
        if ans in ("", "y", "yes"):
            resumed = saved
        else:
            _resume_consume(key, saved.get("uid"))
            print(f"{GRY}Paused run discarded - starting fresh.{RST}")

    if resumed:
        # the whole bank, not just this launch's qs: a practice exam re-samples
        # its 90 Qs every launch, so the paused set must be rebuilt by id
        byid = {qid(tn, q): (tn, q) for (tn, q) in all_questions(_bank(session))}
        byid.update({qid(tn, q): (tn, q) for (tn, q) in qs})
        order = [byid[i] for i in resumed["order"] if i in byid]
        # answered = first `pos` of the OLD order; count only the survivors
        resumed = dict(resumed, pos=sum(1 for i in resumed["order"][:resumed.get("pos", 0)]
                                        if i in byid))
        if len(order) < len(resumed["order"]):
            print(f"{GRY}({len(resumed['order']) - len(order)} question(s) changed "
                  f"since the pause - dropped.){RST}")
        qs = order
        # take ownership: consume the old uid (maybe another device's)
        _resume_consume(key, resumed.get("uid"))
        weak_only_filter = unseen_filter = False
    else:
        weak_only_filter, unseen_filter = weak_only, unseen_only

    if weak_only_filter:
        # weakness is judged against the UNIFIED view (all synced devices)
        merged_q = load_results(session)["questions"]
        qs = [(tn, q) for (tn, q) in qs if is_weak(merged_q.get(qid(tn, q), {}))]
        if not qs:
            print(f"{GRN}No weak spots left here - all cleared.{RST}")
            return
        print(f"{YEL}Weak-drill: {len(qs)} question(s) not yet cleared "
              f"(answer each right {RECENT_N}x in a row to retire it).{RST}")

    if unseen_filter:
        # never-answered questions (new/edited ones you haven't attempted yet)
        merged_q = load_results(session)["questions"]
        qs = [(tn, q) for (tn, q) in qs
              if merged_q.get(qid(tn, q), {}).get("seen", 0) == 0]
        if not qs:
            print(f"{GRN}Nothing unseen - every question here has been answered.{RST}")
            return
        print(f"{CYN}New/unseen drill: {len(qs)} question(s) you haven't "
              f"answered yet.{RST}")

    if shuffle and not mock and not resumed:  # practice exam keeps its PBQs-first order
        random.shuffle(qs)
    total = len(qs)
    score = resumed.get("score", 0.0) if resumed else 0.0
    done = resumed.get("done", 0) if resumed else 0
    missed = resumed.get("missed", []) if resumed else []
    first = resumed.get("pos", 0) if resumed else 0
    uid = f"{DEVICE}-{int(time.time() * 1000)}"
    order_ids = [qid(tn, q) for (tn, q) in qs]
    finished = False

    print(f"\n=== {title}  ({total} questions) ===")
    print(f"{GRY}answer with letters (e.g. 'ac') or type the command · "
          f"/skip · /ref · /flag · /sync · /exit (pauses - resume next time) · /help{RST}\n")
    if resumed:
        print(f"{CYN}Resuming at Q{first + 1}.{RST}\n")

    # the clock only moves when an answer (or skip) registers: walking away
    # mid-question and Ctrl-C'ing hours later adds nothing. Each question is
    # also capped at Q_CAP so an answer typed after a long idle can't blow it up.
    clock = {"used": resumed.get("elapsed", 0) if resumed else 0, "t0": time.time()}

    def tick():
        clock["used"] += min(time.time() - clock["t0"], Q_CAP)
        clock["t0"] = time.time()

    def checkpoint(pos):
        """Save the place after every question, so any exit (even a killed
        terminal) resumes here."""
        _resume_put(key, {
            "uid": uid, "device": DEVICE, "title": title,
            "ts": datetime.now().isoformat(timespec="seconds"),
            "order": order_ids, "pos": pos, "total": total,
            "score": score, "done": done, "missed": _jsonable(missed),
            "elapsed": round(clock["used"], 1)})

    i = first + 1
    try:
        global RUN_QS, RUN_POS
        RUN_QS = list(qs)
        for i, (tn, q) in enumerate(qs, 1):
            RUN_POS = i
            if i <= first:
                continue
            used = clock["used"]
            clock["t0"] = time.time()
            if mock:
                left = mock["mins"] * 60 - used
                if left <= 0:
                    print(f"{RED}⏰ Time's up.{RST}")
                    break
                print(f"{GRY}[{int(left // 60)}:{int(left % 60):02d} left]{RST}")
            else:
                print(f"{GRY}[{int(used // 60)}:{int(used % 60):02d}]{RST}")
            orig = q
            if q.get("parts"):
                res, skipped = ask_parts(q, i, total)
                if skipped:
                    print(f"  {GRY}skipped{RST}")
                    if q["note"]:
                        print(f"  {GRY}› {expand_note(q['note'])}{RST}")
                    print()
                    tick()
                    checkpoint(i)
                    continue
                done += 1
                right = sum(ok for _, _, ok in res)
                frac = right / len(res)
                score += frac
                got_full, partial = right == len(res), 0 < right < len(res)
                col = GRN if got_full else (YEL if partial else RED)
                print(f"\n  {col}PBQ score {right}/{len(res)} "
                      f"({100 * frac:.0f}%){RST}")
                if not got_full:
                    missed.append({"q": q, "parts": res})
            elif q.get("typed"):
                q = relabel_letters(q)   # letter PBQs: fresh letters each run
                ans, skipped = ask_typed(q, i, total)
                want = q["typed"][0]
                if skipped:
                    print(f"  {GRY}skipped - answer: {want}{RST}")
                    if q["note"]:
                        print(f"  {GRY}› {expand_note(q['note'])}{RST}")
                    print()
                    tick()
                    checkpoint(i)
                    continue
                done += 1
                got_full = partial = False
                if typed_ok(ans, q["typed"]):
                    got_full = True
                    score += 1
                    print(f"  {GRN}✓ correct{RST}")
                else:
                    print(f"  {RED}✗ wrong{RST}  answer: {GRN}{want}{RST}")
                    missed.append({"q": q, "typed": ans})
            else:
                got_full, partial, done, score = _ask_mc(
                    q, i, total, shuffle, missed, done, score)
                if got_full is None:
                    tick()
                    checkpoint(i)
                    continue

            if q["note"]:
                print(f"  {GRY}› {expand_note(q['note'])}{RST}")
            print()
            # stats key on the ORIGINAL question (relabelled text would hash
            # to a new id and orphan the stats)
            tick()
            _record(qstats, tn, orig if q.get("typed") else q, got_full, partial)
            save_results(session, data)
            checkpoint(i)
        finished = True
    except (Quit, KeyboardInterrupt, EOFError):
        # save the place even if nothing new was answered since a resume
        # (the resume consumed the old pause; without this it's lost)
        if resumed or done:
            checkpoint(max(first, i - 1))
        print(f"\n{YEL}⏸ Paused at Q{min(i, total)}/{total} - {done} answered, "
              f"{_fmt_secs(clock['used'])} used. Run it again to resume "
              f"(syncs to your other device).{RST}")
        return False
    secs = clock["used"]
    _resume_consume(key, uid)

    if done == 0:
        print(f"{GRY}Nothing answered - not logged.{RST}")
        return

    pct = 100 * score / done
    mode = "+".join(m for m, on in (("weak", weak_only), ("new", unseen_only),
                                    ("shuffle", shuffle)) if on) or "normal"
    if mock:
        mode = "practice_exam"
    # log the run summary BEFORE printing the (interruptible) review
    data["runs"].append({
        "ts": datetime.now().isoformat(timespec="seconds"),
        "title": title,
        **({"test": test_num_of} if test_num_of is not None else {}),
        "score": round(score, 2),
        "answered": done,
        "total": total,
        "pct": round(pct, 1),
        "mode": mode,
        "missed": [m["q"]["q"][:60] for m in missed],
        "secs": round(secs),
        **({"scaled": round(100 + 800 * score / total)} if mock else {}),
    })
    save_results(session, data)

    print("=" * 50)
    head = f"Test {test_num_of} - {title}" if test_num_of else title
    print(f"{CYN}{head}{RST}")
    print(f"Score: {score:.0f}/{done}  =  {pct:.1f}%   {GRY}time: {_fmt_secs(secs)}{RST}")
    if mock:
        # unanswered (timed out / skipped) count as wrong, like the real exam
        scaled = round(100 + 800 * score / total)
        col = GRN if scaled >= mock["pass"] else RED
        mins = secs / 60
        print(f"{col}Scaled: {scaled}/900  (pass {mock['pass']}) - "
              f"{'PASS' if scaled >= mock['pass'] else 'FAIL'}{RST}  "
              f"{GRY}{score:.0f}/{total} right · {mins:.0f} of {mock['mins']} min{RST}")
        by = {}
        for m in missed:
            d = (m["q"].get("obj") or "?")[0]
            by[d] = by.get(d, 0) + 1
        if by:
            print(f"{GRY}misses by domain: " + "  ".join(
                f"D{d} {c}" for d, c in sorted(by.items())) + RST)
    if pct >= 90:
        print(f"{GRN}Solid - knowledge locked.{RST}")
    elif pct >= 80:
        print(f"{YEL}Passing, but tighten the misses.{RST}")
    else:
        print(f"{RED}Gap found - review this topic.{RST}")

    try:
        if missed and CONFIG.get("end_summary", True):
            print(f"\n{YEL}── WHY you missed these ──{RST}")
            for m in missed:
                q = m["q"]
                print(f"\n{RED}✗{RST} {show_stem(q['q'])}")
                if "parts" in m:
                    for j, (pt, ans, ok) in enumerate(m["parts"], 1):
                        mark = f"{GRN}✓{RST}" if ok else f"{RED}✗{RST}"
                        print(f"   {mark} {j}. {pt['prompt']}")
                        if not ok:
                            print(f"      {RED}you:{RST} {ans or '-'}   "
                                  f"{GRN}answer:{RST} {part_answer(pt)}")
                    print(f"   {GRY}why:{RST} {expand_note(q['note'])}")
                    continue
                if "typed" in m:
                    print(f"   {RED}you:{RST}    {m['typed']}")
                    print(f"   {GRN}answer:{RST} {q['typed'][0]}"
                          + (f"  {GRY}(also: {' | '.join(q['typed'][1:])}){RST}"
                             if len(q['typed']) > 1 else ""))
                    print(f"   {GRY}why:{RST} {expand_note(q['note'])}")
                    continue
                for j, (text, is_c) in enumerate(m["opts"]):
                    L = LETTERS[j]
                    chose = L in m["picked"]
                    if is_c and chose:
                        mark = f"{GRN}✓ correct - your answer{RST}"
                    elif is_c:
                        mark = f"{GRN}✓ correct - MISSED{RST}"
                    elif chose:
                        mark = f"{RED}✗ your answer (wrong){RST}"
                    else:
                        mark = ""
                    col = GRN if is_c else (RED if chose else GRY)
                    print(f"   {col}{L}) {text}{RST}  {mark}")
                why = q["note"] or "(no explanation captured - add a *note* line in the bank)"
                print(f"   {GRY}why:{RST} {expand_note(why)}")
            print(f"\n{GRY}Tip: re-drill weak spots with  study {session} weak{RST}")
        elif not missed:
            print(f"\n{GRN}Clean sweep - no misses to review.{RST}")
    except KeyboardInterrupt:
        print()
    print(f"{GRY}(logged to results/{session}@{DEVICE}.json - "
          f"{len(data['runs'])} runs on this device){RST}")


def _trend(history, cap=12):
    """Render an ordered attempt log as a sparkline: ✓ right, ✗ wrong, ~ partial.
    Shows the most recent `cap` attempts (with a leading … if truncated)."""
    if not history:
        return f"{GRY}-{RST}"
    marks = []
    for _, o in history[-cap:]:
        if o == 1:
            marks.append(f"{GRN}✓{RST}")
        elif o == "p":
            marks.append(f"{YEL}~{RST}")
        else:
            marks.append(f"{RED}✗{RST}")
    lead = f"{GRY}…{RST}" if len(history) > cap else ""
    return lead + "".join(marks)


def show_history(session):
    """Recent runs + most-missed questions (with trend) for a session."""
    data = load_results(session)
    runs = data["runs"]
    if not runs:
        print(f"No runs logged yet for {session}.")
        return
    print(f"{CYN}{session}{RST} - recent runs:")
    for r in runs[-15:]:
        ans = r.get("answered", r.get("total", 0))
        pct = r.get("pct")
        pct_s = f"{pct:>5.1f}%" if isinstance(pct, (int, float)) else "    -"
        print(f"  {r.get('ts', '?')}  {pct_s}  ({r.get('score', '?')}/{ans})"
              f" [{r.get('mode', '?')}]  {r.get('title', '')[:34]}")
    # only questions currently in the bank (matches the menu's counts)
    ids = bank_ids(session)
    qstats = {k: v for k, v in data["questions"].items() if k in ids}
    weak = [s for s in qstats.values() if is_weak(s)]
    worst = sorted((s for s in qstats.values() if s.get("wrong", 0) > 0),
                   key=lambda s: (-s["wrong"] / max(s["seen"], 1), -s["wrong"]))
    if worst:
        print(f"\nMost-missed ({len(weak)} still un-cleared):")
        print(f"  {GRY}trend = oldest→newest: {GRN}✓{GRY}=right "
              f"{RED}✗{GRY}=wrong {YEL}~{GRY}=partial (scores 0){RST}")
        for s in worst[:10]:
            rate = 100 * s["wrong"] / max(s["seen"], 1)
            flag = f"{YEL}weak{RST}" if is_weak(s) else f"{GRN}cleared{RST}"
            print(f"  {s['wrong']}/{s['seen']} miss ({rate:.0f}%) [{flag}] "
                  f"{_trend(s.get('history', []))}  {s['q'][:44]}")
    # weakest objectives: accuracy per @obj tag over its answered questions
    obj = {}
    for n, t in _bank(session).items():
        for q in t["questions"]:
            if not q.get("obj"):
                continue
            st = qstats.get(qid(n, q))
            o = obj.setdefault(q["obj"], {"seen": 0, "right": 0, "qs": 0, "done": 0})
            o["qs"] += 1
            if st and st.get("seen"):
                o["done"] += 1
                o["seen"] += st["seen"]
                o["right"] += st.get("right", 0)
    rated = [(100 * o["right"] / o["seen"], k, o) for k, o in obj.items() if o["seen"] >= 4]
    if rated:
        print(f"\nWeakest objectives  {GRY}(accuracy · answers · Qs tried/total){RST}:")
        for pct, k, o in sorted(rated)[:8]:
            col = RED if pct < 70 else (YEL if pct < 85 else GRN)
            print(f"  {col}{pct:3.0f}%{RST}  {k:<11} {GRY}{o['seen']:>3} ans · "
                  f"{o['done']}/{o['qs']} Qs{RST}")
        untried = sorted(k for k, o in obj.items() if o["done"] == 0)
        if untried:
            print(f"  {GRY}never tried: {', '.join(untried)}{RST}")


# ── menus ───────────────────────────────────────────────────────────────────
def pick_session():
    """Session menu. Returns (session, extra_words) - extra_words carries a
    test number / verbs typed after the pick (e.g. '1 weak', '1 3 shuffle') -
    or (None, []) if a tool ran or nothing valid was picked."""
    sessions = list_sessions()
    if not sessions:
        print(f"{RED}No study sessions found under {BANKS_DIR}/"
              f"\nCreate one: banks/<name>/tests.md{RST}")
        return None, []
    cols = _term_cols()
    # name on the LEFT (ellipsized), stat columns right-aligned to the
    # terminal edge. Nothing ever wraps: on narrow screens the least useful
    # columns are dropped first (date, then tests, then Qs).
    rows = []
    for i, s in enumerate(sessions, 1):
        tests = _bank(s)
        data = load_results(s)
        ntests = len(tests)
        nq = sum(len(t["questions"]) for t in tests.values())
        passmark = tests[min(tests)]["passmark"] if tests else DEFAULT_PASS
        mastery = tests[min(tests)]["mastery"] if tests else DEFAULT_MASTERY

        # metrics over questions CURRENTLY in the bank (orphaned stats from
        # reworded/removed Qs are kept on disk but don't count)
        ids = bank_ids(s)
        qstats = {k: v for k, v in data.get("questions", {}).items() if k in ids}
        seen_qs = [st for st in qstats.values() if st.get("seen", 0) > 0]
        seen_total = sum(st.get("seen", 0) for st in seen_qs)
        right_total = sum(st.get("right", 0) for st in seen_qs)
        weak = sum(1 for st in qstats.values() if is_weak(st))

        if seen_qs:
            completion = round(100 * len(seen_qs) / nq) if nq else 0
            # acc = average of each test's latest full-run score, i.e. the
            # 'all' row / newest column of the test menu
            accuracy = latest_avg(data, tests)
            comp = score_cell(completion, passmark, mastery)
            acc = (score_cell(accuracy, passmark, mastery) if accuracy is not None
                   else f"{GRY}  - {RST}")
            wk = f"{YEL}{weak:>4}{RST}" if weak else f"{GRY}   0{RST}"
        else:
            comp = acc = f"{GRY}  - {RST}"
            wk = f"{GRY}   -{RST}"
        runs = data.get("runs") or []
        date = fmt_date(runs[-1]["ts"]) if runs else None
        rows.append({"n": f"{i:>2}. ", "name": s,
                     "done": comp, "acc": acc, "weak": wk,
                     "date": f"{GRY}{(date or '-'):>7}{RST}",
                     "tests": f"{GRY}{ntests:>5}{RST}",
                     "qs": f"{GRY}{nq:>4}{RST}"})
    heads = {"done": "done", "acc": " acc", "weak": "weak", "date": "   last",
             "tests": "tests", "qs": "  Qs"}
    order = ["done", "acc", "weak", "date", "tests", "qs"]
    min_name = 8
    while True:
        stat_w = sum(len(heads[k]) + 1 for k in order)
        if 2 + 4 + min_name + stat_w <= cols or len(order) <= 3:
            break
        for drop in ("date", "tests", "qs"):
            if drop in order:
                order.remove(drop)
                break
    name_w = max(1, cols - 1 - 2 - 4 - stat_w)

    def line(num, name, cells, leader=True):
        # dim dot leader from the name to the stats, so the eye can track
        # across the gap: "mybank · · · · · 59%"
        nm = _ellipsize(name, name_w, min_width=1)
        gap = name_w - _visible_len(nm)
        if leader and gap >= 3:
            # dots on a fixed even-column grid so every row's dots line up
            start = _visible_len(nm)
            dots = "".join("·" if (start + k) % 2 == 1 and k >= 1 and k < gap - 1
                           else " " for k in range(gap))
            pad = f"{GRY}{dots}{RST}"
        else:
            pad = " " * gap
        return f"  {num}{nm}{pad}" + "".join(" " + c for c in cells)

    print(_ellipsize(f"{CYN}Study sessions:{RST}", cols - 1, min_width=1))
    print(GRY + line("    ", "session", [heads[k] for k in order], leader=False) + RST)
    for r in rows:
        print(line(r["n"], r["name"], [r[k] for k in order]))
    print(f"  {GRY}{_ellipsize(chr(39) + '1 weak' + chr(39) + ' · ' + chr(39) + '1 3' + chr(39) + ' · sync · update', cols - 3, min_width=1)}{RST}")
    parts = input("Which session? ").strip().lower().split()
    if not parts:
        print("No such session.")
        return None, []
    head, extra = parts[0], parts[1:]
    if head in ("subnet",):
        cmd_subnet(extra)
        return None, []
    if head.lstrip("/") in ("sync", "update"):
        head = head.lstrip("/")
        raise SystemExit(cmd_sync(pull_code=(head == "update")))
    if head.isdigit() and 1 <= int(head) <= len(sessions):
        return sessions[int(head) - 1], extra
    if head in sessions:
        return head, extra
    print("No such session.")
    return None, []


def _term_cols():
    """Terminal width: $COLUMNS, else the tty size, else 80."""
    env = os.environ.get("COLUMNS")
    if env and env.isdigit():
        return int(env)
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80


def _char_width(c):
    """Terminal cells for one char: 2 for wide/fullwidth (CJK, most emoji),
    0 for combining marks / zero-width joiners, else 1."""
    if unicodedata.combining(c) or c in "\u200b\u200c\u200d\ufe0f":
        return 0
    return 2 if unicodedata.east_asian_width(c) in ("W", "F") else 1


def _visible_len(s):
    """Printed width of s in terminal cells, ignoring ANSI colour codes."""
    return sum(_char_width(c) for c in ANSI_RE.sub("", s))


def _ellipsize(s, width, min_width=10):
    """Trim s to fit `width` terminal cells, ending in '…' when cut.
    Never below `min_width` so a narrow terminal still shows a readable name
    (it wraps instead of vanishing)."""
    width = max(width, min_width)
    if _visible_len(s) <= width:
        return s
    out, used = [], 0
    for c in s:
        w = _char_width(c)
        if used + w > width - 1:
            break
        out.append(c)
        used += w
    return "".join(out) + "…"


def study_time(session):
    """'1day=h:mm 7day=h:mm': run time (secs) summed across ALL devices."""
    import datetime as _dt
    today = _dt.date.today()
    d1 = d7 = 0
    for p in glob.glob(os.path.join(RESULTS_DIR, f"{glob.escape(session)}@*.json")):
        try:
            with open(p) as fh:
                runs = json.load(fh).get("runs", [])
        except (OSError, ValueError):
            continue
        for r in runs:
            try:
                age = (today - _dt.date.fromisoformat(r["ts"][:10])).days
                secs = int(r.get("secs") or 0)
            except (KeyError, ValueError, TypeError):
                continue
            if age == 0:
                d1 += secs
            if 0 <= age < 7:
                d7 += secs
    hm = lambda t: f"{t // 3600}:{t % 3600 // 60:02d}"
    return f"1day={hm(d1)} 7day={hm(d7)}"


def full_runs(data, n, title):
    """FULL runs of test n (every Q answered, not a weak/new drill) = comparable."""
    return [r for r in data["runs"] if (r.get("test") == n if "test" in r
                                        else r.get("title") == title)
            and r.get("answered") == r.get("total")
            and r.get("mode", "normal") in ("normal", "shuffle")]


def latest_avg(data, tests):
    """Average of each test's MOST RECENT full-run score (= 'all' row, newest col)."""
    last = [round(r[-1].get("pct", 0)) for n, t in tests.items()
            if (r := full_runs(data, n, t["title"]))]
    return round(sum(last) / len(last)) if last else None


_MENU_HELP = {}   # session -> show the help block under the menu once


def pick_test(session, tests):
    """Test menu showing each test's last MENU_RUNS run scores; returns the raw pick."""
    data = load_results(session)
    first = tests[min(tests)] if tests else {"passmark": DEFAULT_PASS,
                                             "mastery": DEFAULT_MASTERY}
    print(f"\n{CYN}{session}{RST} - tests  "
          f"{GRY}(pass {first['passmark']}%"
          + (f" = exam {MOCK[session]['pass']}/900" if session in MOCK else "")
          + f" · master {first['mastery']}%)"
          f"  | time: {study_time(session)}{RST}:")
    cols = _term_cols()
    # columns: last MENU_RUNS full-run scores (NEWEST first) | last run date
    #          | question count | test number + title. Each score cell is 4 wide.
    sw = 5 * MENU_RUNS - 1
    head = "newest" + "older".rjust(sw - 6)
    print(f"  {GRY}{head}|{'date':^7}|{'Qs':^3}| {'#':>2}| test{RST}")
    cols_pct = [[] for _ in range(MENU_RUNS)]   # per-column scores for 'all'
    paused = _resume_all()
    for n in sorted(tests):
        runs = full_runs(data, n, tests[n]["title"])
        last = [round(r.get("pct", 0)) for r in runs[-MENU_RUNS:]][::-1]
        for k, p in enumerate(last):
            cols_pct[k].append(p)
        cells = [score_cell(p, tests[n]["passmark"], tests[n]["mastery"])
                 for p in last] + [f"{GRY}  - {RST}"] * (MENU_RUNS - len(last))
        date = fmt_date(runs[-1]["ts"] if runs else
                        data["tests"].get(str(n), {}).get("last"))
        dcol = f"{date:>7}" if date else "      -"
        qc = f"{len(tests[n]['questions']):>3}"
        mark = f"{YEL}⏸{RST}" if f"{session}:T{n}" in paused else " "
        left = f"  {' '.join(cells)} {GRY}{dcol}{RST} {GRY}{qc}{RST} {mark}{n:>2}. "
        name = _ellipsize(tests[n]["title"],
                          min(TITLE_MAX, cols - _visible_len(left)))
        print(f"{left}{name}")
    total = sum(len(t['questions']) for t in tests.values())
    # 'all' row: each column = average of the tests that have a score there
    avgs = [score_cell(round(sum(c) / len(c)), first["passmark"], first["mastery"])
            if c else f"{GRY}  - {RST}" for c in cols_pct]
    print(f"  {GRY}{'─' * min(sw + 20 + TITLE_MAX, cols - 3)}{RST}")
    # 'all' row doubles as the footer: practice-exam scaled scores + '? help' at the right
    left = f"  {' '.join(avgs)} {GRY}      - {total:>3}{RST}   "
    mid = ""
    if session in MOCK:
        pm = MOCK[session]["pass"]
        ps = [round(r["pct"]) for r in data.get("runs", [])
              if r.get("mode") == "practice_exam" and "pct" in r][-6:][::-1]
        mid = "practice: " + (" ".join(score_cell(v, round(pm / 9), first["mastery"]).strip()
                                       for v in ps) if ps else f"{GRY}none yet{RST}")
    tail = f"{GRY}? help{RST}"
    gap = max(2, min(sw + 20 + TITLE_MAX, cols - 3) + 2
              - _visible_len(left) - _visible_len(mid) - _visible_len(tail))
    print(f"{left}{mid}{' ' * gap}{tail}")
    if _MENU_HELP.pop(session, False):
        menu_help(session)
    return input("Which test? ").strip()


def menu_help(session):
    """The test-menu options that don't fit on the one-line footer."""
    print(f"\n{CYN}Test menu keys{RST}")
    print("  3            run Test 3")
    print("  a            all tests pooled (the bottom row)")
    if session in DRILL_BANKS:
        extra = " (hard: all /n, wildcards, hosts→prefix)" if DRILL_BANKS[session] else ""
        print(f"  s            subnetting drill, generated{extra} · 'study subnet history'")
    if session in MOCK:
        c = MOCK[session]
        print(f"  p            practice exam: {c['n']} Q · {c['mins']} min · domain-weighted · /900")
    print("  weak / new   whole session: missed Qs / never-seen Qs")
    print("  3 weak       add to a test: '3 weak', '3 new', '3 shuffle'")
    print("  history      past runs, weak spots, weakest objectives")
    print("  /sync        push + pull records (also works mid-quiz)\n")


def mock_questions(session, tests):
    """Domain-weighted random pick for a mock exam (MOCK[session])."""
    cfg = MOCK[session]
    pool = {}
    for n, q in all_questions(tests):
        d = (q.get("obj") or "?")[0]
        if d in cfg["weights"]:
            pool.setdefault(d, []).append((n, q))
    tot = sum(cfg["weights"].values())
    want = {d: round(cfg["n"] * w / tot) for d, w in cfg["weights"].items()}
    # fix rounding so the counts add up to n exactly
    while sum(want.values()) != cfg["n"]:
        d = max(cfg["weights"], key=cfg["weights"].get)
        want[d] += 1 if sum(want.values()) < cfg["n"] else -1
    # multi-part PBQs come first, like the real exam; they replace regular
    # questions from their own domain so the weighting holds
    pbqs = [(n, q) for n, q in all_questions(tests) if q.get("parts")]
    first = random.sample(pbqs, min(cfg.get("pbq", 0), len(pbqs)))
    for _, q in first:
        d = (q.get("obj") or "?")[0]
        if want.get(d):
            want[d] -= 1
    out = []
    for d, k in want.items():
        cand = [x for x in pool.get(d, []) if not x[1].get("parts")]
        out += random.sample(cand, min(k, len(cand)))
    random.shuffle(out)
    return first + out


def all_questions(tests):
    """Every (test_num, question) in a bank, in test order."""
    return [(n, q) for n in sorted(tests) for q in tests[n]["questions"]]


# ── settings command ────────────────────────────────────────────────────────
def cmd_set(rest):
    """`set` with no args lists this host's settings; `set key value` changes one."""
    cfg = load_config()
    truthy = {"on": True, "off": False, "true": True, "false": False,
              "yes": True, "no": False, "1": True, "0": False}
    if not rest:
        print(f"{CYN}settings for {DEVICE}{RST}  "
              f"{GRY}(results/settings@{DEVICE}.json - synced){RST}")
        for k in sorted(DEFAULT_SETTINGS):
            v = cfg.get(k, DEFAULT_SETTINGS[k])
            print(f"  {k} = {GRN if v else GRY}{str(v).lower()}{RST}")
        print(f"{GRY}change: study set <key> on|off{RST}")
        return 0
    key = rest[0]
    if key not in DEFAULT_SETTINGS:
        print(f"{RED}unknown setting '{key}'. known: {', '.join(sorted(DEFAULT_SETTINGS))}{RST}")
        return 1
    if len(rest) < 2:
        print(f"{RED}give a value: study set {key} on|off{RST}")
        return 1
    val = rest[1].lower()
    if val not in truthy:
        print(f"{RED}value must be on/off (got '{rest[1]}'){RST}")
        return 1
    cfg[key] = truthy[val]
    save_config(cfg)
    print(f"{GRN}{key} = {str(cfg[key]).lower()}{RST}  "
          f"{GRY}(saved to results/settings@{DEVICE}.json){RST}")
    return 0


# ── subnetting drill ────────────────────────────────────────────────────────
CHEAT = """\
128 64  32  16  8   4   2   1   -block
128 192 224 240 248 252 254 255 -mask
/1  /2  /3  /4  /5  /6  /7  /8  -octet1
/9  /10 /11 /12 /13 /14 /15 /16 -octet2
/17 /18 /19 /20 /21 /22 /23 /24 -octet3
/25 /26 /27 /28 /29 /30 /31 /32 -octet4

16  32  48  64  -16 x tables
80  96  112 128
144 160 176 192
208 224 240 256

hosts: octet-4 row = block - 2
octet-3 row doubles from /24:
/24 254    /23 510    /22 1022
/21 2046   /20 4094   /19 8190
/18 16382  /17 32766  /16 65534"""


def print_cheat():
    """Print the subnetting table (the drill's /ref)."""
    print(f"\n{CYN}{CHEAT}{RST}\n")


def ref_path(session):
    """Optional per-bank quick reference: banks/<session>/ref.md."""
    return os.path.join(bank_dir(session), "ref.md")


_ACRO = {}


def acronyms(session):
    """{ACRONYM: expansion} from banks/<s>/acronyms.md ('X = expansion' lines)."""
    if session not in _ACRO:
        d = {}
        path = os.path.join(os.path.dirname(bank_path(session)), "acronyms.md")
        if os.path.exists(path):
            for ln in open(path, encoding="utf-8"):
                a, sep, e = ln.strip().partition(" = ")
                if sep and not a.startswith(("#", "<")):
                    d[a] = e
        _ACRO[session] = d
    return _ACRO[session]


def expand_note(note):
    """Expand each glossary acronym in a note at its first mention, unless
    the note already expands it ('X (...)')."""
    d = acronyms(REF_SESSION) if REF_SESSION else {}
    if not note or not d:
        return note
    seen = set()

    def sub(m):
        w = m.group(0)
        key = w if w in d else (w[:-1] if w.endswith("s") and w[:-1] in d else None)
        if not key or key in seen or not re.search(r"[A-Z].*[A-Z]|[A-Z].*\d", key):
            return w
        seen.add(key)
        if re.match(r"\s*\(", note[m.end():]):
            return w
        # already spelled out right after: 'LUNs, Logical Unit Numbers'
        first = d[key].split()[0].lower() if d[key].split() else ""
        if first and note[m.end():].lstrip(",: -–").lower().startswith(first):
            return w
        if note[:m.start()].rstrip().endswith("("):
            return f"{w}: {d[key]}"      # already inside brackets: no nesting
        return f"{w} ({d[key]})"
    return re.sub(r"(?<![\w/-])[A-Za-z0-9][A-Za-z0-9+-]*[A-Za-z0-9](?![\w-])", sub, note)


def print_ref(session, quiz=False):
    """Show a bank's ref.md (mnemonics, key tables) - for when you're stuck.
    quiz=True (in-quiz /ref): prefer banks/<s>/scratch.md, your own sheet."""
    p = ref_path(session) if session else None
    if quiz and session:
        sp = os.path.join(bank_dir(session), "scratch.md")
        if os.path.isfile(sp):
            p = sp
    if p and os.path.isfile(p):
        with open(p, encoding="utf-8") as f:
            print(f"\n{CYN}{f.read().rstrip()}{RST}\n")
    else:
        print(f"  {GRY}no ref for {session} (add banks/{session}/ref.md){RST}")


def _ip_to_int(o):
    """[a, b, c, d] octets -> 32-bit int."""
    return (o[0] << 24) | (o[1] << 16) | (o[2] << 8) | o[3]


def _int_to_ip(n):
    """32-bit int -> dotted-quad string."""
    return ".".join(str((n >> s) & 0xFF) for s in (24, 16, 8, 0))


def _subnet_facts(octets, cidr):
    """Return the derived facts for host IP `octets` with prefix `cidr`.
    /31 = point-to-point link, 2 usable, no network/broadcast (RFC 3021);
    /32 = single host route, 1 usable."""
    ip = _ip_to_int(octets)
    mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF if cidr else 0
    network = ip & mask
    broadcast = network | (~mask & 0xFFFFFFFF)
    total = 1 << (32 - cidr)
    if cidr >= 31:
        usable, first, last = total, network, broadcast
    else:
        usable, first, last = total - 2, network + 1, broadcast - 1
    return {
        "mask": _int_to_ip(mask),
        "network": _int_to_ip(network),
        "broadcast": _int_to_ip(broadcast),
        "first": _int_to_ip(first),
        "last": _int_to_ip(last),
        "usable": usable,
        "block": total,
        "wildcard": _int_to_ip(~mask & 0xFFFFFFFF),
    }


def _random_subnet(rng):
    """Pick a plausible private IP + a CIDR that isn't trivial.
    The host is always a VALID host (never the network/broadcast address)."""
    base = rng.choice([
        [10, rng.randint(0, 255), rng.randint(0, 255), rng.randint(1, 254)],
        [172, rng.randint(16, 31), rng.randint(0, 255), rng.randint(1, 254)],
        [192, 168, rng.randint(0, 255), rng.randint(1, 254)],
    ])
    cidr = rng.choice([8, 12, 14, 16, 17, 18, 19, 20, 21, 22, 23,
                       24, 25, 26, 27, 28, 29, 30])
    f = _subnet_facts(base, cidr)
    lo = _ip_to_int([int(x) for x in f["first"].split(".")])
    hi = _ip_to_int([int(x) for x in f["last"].split(".")])
    h = rng.randint(lo, hi)
    return [(h >> s) & 0xFF for s in (24, 16, 8, 0)], cidr


SUBNET_PATH = os.path.join(RESULTS_DIR, f"subnet@{DEVICE}.json")
# bank -> subnet drill in its menu: exam.json "subnet_drill": "basic" | "hard"
DRILL_BANKS = {b: c.get("subnet_drill") == "hard" for b, c in EXAMS.items() if c.get("subnet_drill")}


def _subnet_save(asked, score, misses, mode="basic"):
    """Append a drill run to this device's results/subnet@<device>.json."""
    if not asked:
        return
    data = _read_json(SUBNET_PATH) or {"runs": []}
    data["runs"].append({
        "ts": datetime.now().isoformat(timespec="seconds"),
        "asked": asked, "score": score,
        "pct": round(100 * score / asked, 1), "missed": misses,
        "mode": mode})
    os.makedirs(RESULTS_DIR, exist_ok=True)
    _atomic_write_json(SUBNET_PATH, data)


def subnet_history():
    """Past drill runs from every device, plus which /n and fields you miss."""
    runs = []
    for p in sorted(glob.glob(os.path.join(RESULTS_DIR, "subnet@*.json"))):
        dev = os.path.basename(p)[7:-5]
        for r in (_read_json(p) or {}).get("runs", []):
            runs.append((r["ts"], dev, r))
    if not runs:
        print(f"{GRY}no subnet drill runs yet{RST}")
        return 0
    runs.sort(key=lambda x: x[0])
    print(f"{CYN}Subnet drill history{RST}")
    for ts, dev, r in runs[-15:]:
        print(f"  {fmt_date(ts)}  {r['score']:>3}/{r['asked']:<3} "
              f"{r['pct']:>5.1f}%  {({'net+': 'basic', 'ccna': 'hard'}.get(r.get('mode'), r.get('mode')) or 'basic'):<5} {GRY}{dev}{RST}")
    by_cidr, by_field = {}, {}
    for _, _, r in runs:
        for m in r.get("missed", []):
            by_cidr[m["cidr"]] = by_cidr.get(m["cidr"], 0) + 1
            by_field[m["field"]] = by_field.get(m["field"], 0) + 1
    tot = sum(r["asked"] for _, _, r in runs)
    ok = sum(r["score"] for _, _, r in runs)
    print(f"\n  overall {ok}/{tot} ({100 * ok / tot:.0f}%)")
    if by_cidr:
        top = sorted(by_cidr.items(), key=lambda x: -x[1])[:6]
        print("  most-missed /n:   " + "  ".join(f"/{c}×{k}" for c, k in top))
        top = sorted(by_field.items(), key=lambda x: -x[1])
        print("  most-missed type: " + "  ".join(f"{f}×{k}" for f, k in top))
    return 0


def _random_subnet_at(rng, cidr):
    """A valid host octet list for a given /cidr."""
    while True:
        o, _ = _random_subnet(rng)
        f = _subnet_facts(o, cidr)
        lo = _ip_to_int([int(x) for x in f["first"].split(".")])
        hi = _ip_to_int([int(x) for x in f["last"].split(".")])
        if hi >= lo:
            h = rng.randint(lo, hi)
            r = [(h >> s) & 0xFF for s in (24, 16, 8, 0)]
            # keep it a private address (a /8 around 192.168 isn't)
            if (r[0] == 10 or (r[0] == 172 and 16 <= r[1] <= 31)
                    or r[:2] == [192, 168]):
                return r


def cmd_subnet(rest):
    """Interactive subnetting practice: given IP/CIDR, work out the facts.
    Usage: study subnet [hard] [N] | subnet history
    hard = every /8-/30, wildcard masks, 'N hosts -> smallest /n'."""
    if rest and rest[0] in ("history", "hist", "h"):
        return subnet_history()
    hard = "hard" in rest or "ccna" in rest
    nums = [w for w in rest if w.isdigit()]
    n = max(1, int(nums[0])) if nums else 10
    rng = random.Random()
    if hard:
        print(f"{YEL}hard mode{RST} {GRY}- all prefixes, wildcard masks, hosts→prefix{RST}")
    print(f"{CYN}Subnetting drill{RST} {GRY}- {n} questions. Type your answer, "
          f"'q' to quit, Enter to see the answer, /ref for the table.{RST}\n")
    fields = [
        ("network", "Network (subnet) address"),
        ("broadcast", "Broadcast address"),
        ("first", "First usable host"),
        ("last", "Last usable host"),
        ("usable", "Number of usable hosts"),
    ]
    score = 0
    asked = 0
    misses = []

    def summary(head):
        """Print the running score under a heading, and save the run."""
        print(f"{'=' * 40}\n{CYN}{head}{RST} {score}/{asked} correct "
              f"({100 * score / max(asked, 1):.0f}%)")
        _subnet_save(asked, score, misses, "hard" if hard else "basic")
        if asked:
            print(f"{GRY}(logged to results/subnet@{DEVICE}.json - "
                  f"'study subnet history' to review){RST}")

    def ask_one(label):
        """Prompt; /ref shows the table. None = quit."""
        try:
            while True:
                a = input(f"   {label}? ").strip()
                if a.lower() not in ("/ref", "/r"):
                    break
                print_cheat()
        except (EOFError, KeyboardInterrupt):
            print()
            return None
        return None if a.lower() in ("q", "quit", "exit") else a

    for i in range(1, n + 1):
        if hard and rng.random() < 0.25:
            # design question: smallest subnet that fits N hosts
            bits = rng.randint(2, 14)
            need = rng.randint((1 << (bits - 1)) - 1, (1 << bits) - 2)
            want = f"/{32 - bits}"
            print(f"{CYN}Q{i}/{n}{RST}  A LAN needs {GRN}{need}{RST} usable hosts.")
            ans = ask_one("Smallest prefix that fits (e.g. /26)")
            if ans is None:
                summary("Subnet drill stopped:")
                return 0
            asked += 1
            if ans.replace(" ", "").lstrip("/") == want[1:]:
                print(f"   {GRN}✓{RST}")
                score += 1
            else:
                print(f"   {RED}✗ {want}{RST}")
                misses.append({"q": f"{need} hosts", "cidr": 32 - bits,
                               "field": "prefix", "ans": ans})
            print(f"   {GRY}└─ {want} = {(1 << bits) - 2} usable; "
                  f"/{33 - bits} only {(1 << (bits - 1)) - 2}{RST}\n")
            continue
        octets, cidr = _random_subnet(rng)
        if hard:
            cidr = rng.randint(8, 30)
            octets = _random_subnet_at(rng, cidr)
        host = _int_to_ip(_ip_to_int(octets))
        f = _subnet_facts(octets, cidr)
        print(f"{CYN}Q{i}/{n}{RST}  Host {GRN}{host}/{cidr}{RST}")
        # ask 2 random facts per question to keep it snappy
        # huge host counts (/8-/16) barely show up on Net+: skip them there
        pool = fields if (cidr >= 17 or hard) else [x for x in fields if x[0] != "usable"]
        if hard:
            pool = pool + [("wildcard", "Wildcard mask")]
        for key, label in rng.sample(pool, 2):
            want = str(f[key])
            try:
                while True:
                    ans = input(f"   {label}? ").strip()
                    if ans.lower() not in ("/ref", "/r"):
                        break
                    print_cheat()
            except (EOFError, KeyboardInterrupt):
                print()
                summary("Subnet drill stopped:")
                return 0
            if ans.lower() in ("q", "quit", "exit"):
                summary("Subnet drill stopped:")
                return 0
            asked += 1
            if ans == want:
                print(f"   {GRN}✓{RST}")
                score += 1
            else:
                print(f"   {RED}✗ {want}{RST}")
                misses.append({"q": f"{host}/{cidr}", "cidr": cidr,
                               "field": key, "ans": ans})
        # always show the full worked solution
        print(f"   {GRY}└─ mask {f['mask']} · wildcard {f['wildcard']} · network {f['network']} · broadcast {f['broadcast']} "
              f"· hosts {f['first']}–{f['last']} · {f['usable']} usable "
              f"· block size {f['block']}{RST}\n")
    summary("Subnet drill done:")
    return 0


# ── git sync ────────────────────────────────────────────────────────────────
def _git(args, capture=False, where=None):
    """Run a git command in the data repo (or `where`). Returns (rc, out)."""
    env = dict(os.environ)
    # let pinentry find the terminal so a gpg-backed git credential can be decrypted
    try:
        tty = os.ttyname(sys.stdin.fileno())
        env["GPG_TTY"] = tty
        subprocess.run(["gpg-connect-agent", "updatestartuptty", "/bye"],
                       cwd=where or DATA, env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass
    r = subprocess.run(["git", *args], cwd=where or DATA, env=env,
                       text=True,
                       stdout=(subprocess.PIPE if capture else None),
                       stderr=(subprocess.STDOUT if capture else None))
    return r.returncode, (r.stdout or "")


def _in_repo():
    """True if DATA is inside a git work tree (it may be a subfolder of one)."""
    if not os.path.isdir(DATA):
        return False
    r = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=DATA,
                       capture_output=True, text=True)
    return r.returncode == 0 and r.stdout.strip() == "true"


def _has_remote():
    if not _in_repo():
        return False
    rc, out = _git(["remote"], capture=True)
    return rc == 0 and bool(out.strip())


def cmd_init(args):
    """study init [URL]: set up the data repo. URL = clone your existing data repo
    (GitHub, Gitea, any git remote); no URL = new local repo, add a remote later
    with `study init URL`."""
    url = args[0] if args else ""
    if _in_repo():
        if not url:
            print(f"data repo already at {DATA}")
            return 0
        rc, _ = _git(["remote", "add", "origin", url])
        if rc != 0:
            rc, _ = _git(["remote", "set-url", "origin", url])
        if rc != 0:
            return rc
        _, br = _git(["symbolic-ref", "--short", "HEAD"], capture=True)
        br = br.strip() or "main"
        if _git(["fetch", "-q", "origin"])[0] == 0 and \
                _git(["rev-parse", "-q", "--verify", f"origin/{br}"], capture=True)[0] == 0:
            rc, _ = _git(["pull", "--rebase", "--allow-unrelated-histories", "origin", br])
            if rc != 0:
                print(f"{RED}could not merge with {url} (rc {rc}){RST}")
                return rc
        rc, _ = _git(["push", "-u", "origin", br])
        return rc
    # inside an existing repo (DATA is a new subfolder of it): just make the folder
    up = DATA
    while up and not os.path.isdir(up):
        up = os.path.dirname(up)
    inside = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=up or "/",
                            capture_output=True, text=True).stdout.strip() == "true"
    if inside and not url:
        for d in ("banks", "results"):
            os.makedirs(os.path.join(DATA, d), exist_ok=True)
            open(os.path.join(DATA, d, ".keep"), "a").close()
        print(f"{GRY}{DATA} is inside an existing git repo; using that repo{RST}")
    elif url:
        rc = subprocess.run(["git", "clone", url, DATA]).returncode
        if rc != 0:
            return rc
        # remote HEAD may point at a branch that doesn't exist (e.g. bare repo
        # defaulting to master while data was pushed to main): track what's there
        if _git(["rev-parse", "-q", "--verify", "HEAD"], capture=True)[0] != 0:
            _, out = _git(["branch", "-r", "--format=%(refname:short)"], capture=True)
            rb = [b for b in out.split() if b != "origin/HEAD" and "/" in b]
            pick = "origin/main" if "origin/main" in rb else (rb[0] if rb else "")
            if pick:
                _git(["checkout", "-q", "-B", pick.split("/", 1)[1], "--track", pick])
    else:
        os.makedirs(os.path.join(DATA, "banks"), exist_ok=True)
        os.makedirs(os.path.join(DATA, "results"), exist_ok=True)
        subprocess.run(["git", "init", "-q", DATA])
        _git(["symbolic-ref", "HEAD", "refs/heads/main"])   # works on git < 2.28 too
        _git(["config", "init.defaultBranch", "main"])
        open(os.path.join(DATA, "banks", ".keep"), "a").close()
        open(os.path.join(DATA, "results", ".keep"), "a").close()
        _git(["add", "-A"])
        rc, _ = _git(["commit", "-qm", "study data"])
        if rc != 0:
            print(f"{YEL}first commit failed. Set git user.name and user.email, then: "
                  f"git -C {DATA} commit -m 'study data'{RST}")
    if not os.environ.get("STUDY_DATA") and not os.path.exists(CONF_FILE):
        os.makedirs(os.path.dirname(CONF_FILE), exist_ok=True)
        with open(CONF_FILE, "w", encoding="utf-8") as f:
            f.write(f'data = "{DATA}"\nauto_update = true\n')
    print(f"{GRN}✓ data repo at {DATA}{RST}. Put banks in banks/<name>/tests.md.")
    return 0


def cmd_sync(pull_code=False):
    """`sync` = commit + push THIS device's results and any bank changes (if lint passes), pull others'.
    `update` (pull_code=True) = pull the engine, then your data repo."""
    if pull_code:
        print(f"{CYN}study update{RST} {GRY}- engine, then your data{RST}")
        old = _version()
        rc, _ = _git(["pull", "-q", "--ff-only"], where=HERE)
        erc = rc
        if rc != 0:
            print(f"{RED}engine pull failed (rc {rc}){RST}")
        else:
            print(f"engine {old}" + (f" -> {_version()}" if _version() != old else " (latest)"))
        if not _in_repo():
            print(f"{YEL}no data repo at {DATA}. Run: study init{RST}")
            return erc
        if not _has_remote():
            print(f"{GRY}data is local only{RST}")
            return erc
        rc, _ = _git(["pull", "--rebase", "--autostash"])
        print(f"{GRN}✓ data up to date{RST}" if rc == 0 else f"{RED}data pull failed (rc {rc}){RST}")
        return rc or erc
    if not _in_repo():
        print(f"{RED}no data repo at {DATA}. Run: study init{RST}")
        return 1

    print(f"{CYN}study sync{RST} {GRY}- syncing study records for {DEVICE}{RST}")
    # stage + commit ONLY this device's own files (per-device → never conflict).
    # explicit literal paths (no glob) so an odd hostname can't match peers.
    own = sorted(os.path.relpath(p, DATA) for p in
                 glob.glob(os.path.join(RESULTS_DIR, f"*@{glob.escape(DEVICE)}.json")))
    if not own:
        print(f"{GRY}no local records yet{RST}")
    else:
        spec = [f":(literal){p}" for p in own]
        rc, out = _git(["add", "--", *spec], capture=True)
        if rc != 0:
            print(f"{RED}git add failed (rc {rc}): {out.strip()}{RST}")
            return rc
        rc, _ = _git(["diff", "--cached", "--quiet", "--", *spec], capture=True)
        if rc != 0:  # there are staged changes
            rc, _ = _git(["commit", "-q", "-m", f"study records: {DEVICE} progress",
                          "--", *spec])
            if rc != 0:
                print(f"{RED}commit failed (rc {rc}){RST}")
                return rc
            print(f"{GRN}✓ committed local progress{RST}")
        else:
            print(f"{GRY}no local changes to commit{RST}")
    # private banks: commit changes under banks/ too, but only if every bank lints clean
    held = 0
    _, ch = _git(["status", "--porcelain", "--", "banks"], capture=True)
    if ch.strip():
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            bad = lint()
        if bad:
            print(f"{YEL}bank changes NOT pushed: lint failed (run study --lint){RST}")
            held = 1
        else:
            _git(["add", "-A", "--", "banks"])
            rc, _ = _git(["commit", "-q", "-m", f"banks: update from {DEVICE}", "--", "banks"])
            if rc == 0:
                print(f"{GRN}✓ committed bank changes{RST}")
    # rebase: both devices may have committed since last sync; their files
    # never overlap, so replaying ours on top is always clean.
    if not _has_remote():
        print(f"{GRY}no remote set: records committed locally (study init URL to add one){RST}")
        return held
    rc, _ = _git(["pull", "--rebase", "--autostash"])
    if rc != 0:
        print(f"{RED}pull failed (rc {rc}) - resolve by hand, then re-run.{RST}")
        return rc
    rc, _ = _git(["push", "origin", "HEAD"])
    if rc == 0:
        print(f"{GRN}✓ synced - records pushed + pulled{RST}")
        rc = held
    else:
        print(f"{RED}push failed (rc {rc}){RST}")
    return rc


# ── CLI ─────────────────────────────────────────────────────────────────────
VERBS = {"shuffle", "weak", "history", "new", "unseen", "mock", "practice_exam", "exam"}


def parse_words(words):
    """Split CLI/menu words into (positional, flags). Verbs are
    order-independent; 'unseen' is an alias of 'new'."""
    import difflib
    low = []
    for w in words:
        lw = w.lower()
        if lw not in VERBS and not lw.isdigit() and not lw.startswith("--") and len(lw) >= 3:
            m = difflib.get_close_matches(lw, VERBS, n=1, cutoff=0.75)
            if m:
                print(f"  ('{w}' -> '{m[0]}')")
                lw = m[0]
        low.append(lw)
    words = low
    flags = {"shuffle": "shuffle" in low, "weak": "weak" in low,
             "new": "new" in low or "unseen" in low, "history": "history" in low,
             "mock": bool({"mock", "practice_exam", "exam"} & set(low))}
    pos = [w for w in words if w.lower() not in VERBS and not w.startswith("--")]
    return pos, flags


def parse_queue(pos, tests):
    """'5-10', '5 7 10', '5,7,10' (mixable) -> [5,6,..]; None unless 2+ valid tests."""
    txt = re.sub(r"\s*-\s*", "-", " ".join(pos))      # '5 - 10' -> '5-10'
    toks = [t for t in re.split(r"[\s,]+", txt) if t]
    if not toks or len(toks) == 1 and "-" not in toks[0]:
        return None                                     # single test: normal path
    out, bad = [], []
    top = max(tests) if tests else 0
    for tok in toks:
        lo, _, hi = tok.partition("-")
        if not (lo.isdecimal() and (not hi or hi.isdecimal())):
            return None                                 # not a queue at all
        a, b = sorted((int(lo), int(hi or lo)))
        rng = [n for n in range(a, min(b, top) + 1)]
        out += [n for n in rng if n in tests]
        if int(lo) not in tests or (hi and int(hi) not in tests):
            bad.append(tok)
    out = list(dict.fromkeys(out))
    if bad:
        print(f"{GRY}(no such test: {', '.join(bad)} - skipped){RST}")
    return out or None


def run_queue(session, tests, queue, shuffle, weak, new):
    """Run several tests back to back; stop if one is quit."""
    for k, n in enumerate(queue):
        if k:
            print(f"\n{CYN}── next in queue: test {n} ({k + 1}/{len(queue)}) ──{RST}")
        if run(session, [(n, q) for q in tests[n]["questions"]], n,
               tests[n]["title"], shuffle, weak_only=weak,
               unseen_only=new) is False:
            print(f"{GRY}Queue stopped.{RST}")
            break


def dispatch(session, sel, flags):
    """Run whatever (test pick + flags) names within one session."""
    if flags["history"]:
        show_history(session)
        return
    tests = _bank(session)
    if not tests:
        print(f"{RED}No tests parsed in {bank_path(session)}{RST}")
        return
    if flags.get("mock"):
        if session not in MOCK:
            print(f"{RED}No practice exam set up for {session}.{RST}")
            return
        cfg = MOCK[session]
        qs = mock_questions(session, tests)
        print(f"{CYN}PRACTICE EXAM - {len(qs)} questions, {cfg['mins']} minutes, "
              f"weighted by domain. Pass = {cfg['pass']}/900.{RST}")
        print(f"{GRY}Skipped or unanswered questions count as wrong.{RST}")
        run(session, qs, None, f"{session} - practice exam", shuffle=True, mock=cfg)
        return
    weak, new, shuffle = flags["weak"], flags["new"], flags["shuffle"]
    if sel is not None and not sel.isdecimal():      # CLI range: '31-34', '5,7'
        queue = parse_queue([sel], tests)
        if queue:
            return run_queue(session, tests, queue, shuffle, weak, new)
    if sel is None and (weak or new):   # bare weak/new = whole session
        label = "weak drill" if weak else "new/unseen"
        run(session, all_questions(tests), None, f"{session} - {label}",
            shuffle, weak_only=weak, unseen_only=new)
        return
    if sel is None:
        try:
            picked = pick_test(session, tests)
        except (KeyboardInterrupt, EOFError):
            print()
            return
        pos, more = parse_words(picked.split())
        flags = {k: flags[k] or more[k] for k in flags}
        weak, new, shuffle = flags["weak"], flags["new"], flags["shuffle"]
        queue = parse_queue(pos, tests)
        if queue:
            return run_queue(session, tests, queue, shuffle, weak, new)
        sel = pos[0].lower() if pos else ("a" if (weak or new) else "")
        if flags["history"]:
            show_history(session)
            return
        if sel == "/sync":
            cmd_sync()
            return dispatch(session, None, flags)
        if sel.lstrip("/") in ("?", "h", "help"):
            _MENU_HELP[session] = True
            return dispatch(session, None, flags)
        if sel in ("p", "m", "mock", "practice_exam", "exam") and session in MOCK:
            dispatch(session, None, dict(flags, mock=True))
            return
    if sel in ("s", "subnet") and session in DRILL_BANKS:
        cmd_subnet(["hard"] if DRILL_BANKS[session] else [])
        return
    if sel in ("a", "all"):
        run(session, all_questions(tests), None, f"{session} - ALL tests",
            shuffle, weak_only=weak, unseen_only=new)
    elif sel.isdecimal() and int(sel) in tests:
        n = int(sel)
        run(session, [(n, q) for q in tests[n]["questions"]], n,
            tests[n]["title"], shuffle, weak_only=weak, unseen_only=new)
    else:
        print("No such test.")


def set_title(name):
    """Name the terminal tab (Konsole shows the process name, not 'python3')."""
    try:
        import ctypes
        ctypes.CDLL(None).prctl(15, name.encode()[:15], 0, 0, 0)  # PR_SET_NAME
    except Exception:
        pass
    if sys.stdout.isatty():
        sys.stdout.write(f"\033]30;{name}\007\033]2;{name}\007")  # Konsole tab + window
        sys.stdout.flush()


def main():
    """CLI entry: tools (lint/set/sync/update/subnet), else a session run."""
    args = sys.argv[1:]

    if args[:1] in (["--version"], ["version"]):
        print(_version())
        sys.exit(0)
    if not (args and args[0] in ("update", "sync", "init", "--lint")):
        _auto_update()

    if "--lint" in args:
        sys.exit(lint())

    # settings:  study set               (list this host's settings)
    #            study set <key> <value>  (change one; value on/off/true/…)
    if args and args[0] == "set":
        sys.exit(cmd_set(args[1:]))

    # init = set up the data repo; sync = push/pull records; update = engine + data
    if args and args[0] in ("flags", "flagged"):
        sys.exit(cmd_flags())
    if args and args[0] == "build":
        if len(args) != 2 or not os.path.isdir(os.path.join(bank_dir(args[1]), "drafts")):
            sys.exit(f"usage: study build BANK  (needs {BANKS_DIR}/BANK/drafts/*.txt)")
        rc = subprocess.run([sys.executable, os.path.join(HERE, "tools", "build.py"), args[1], DATA,
                             bank_dir(args[1])]).returncode
        sys.exit(rc if rc else (1 if lint() else 0))
    if args and args[0] == "init":
        sys.exit(cmd_init(args[1:]))
    if args and args[0] in ("sync", "update"):
        sys.exit(cmd_sync(pull_code=(args[0] == "update")))

    # subnetting practice generator
    if args and args[0] in ("subnet", "subnetting"):
        sys.exit(cmd_subnet(args[1:]))
    if args and args[0] == "ref":
        if len(args) < 2 or args[1] in ("subnet", "subnetting"):
            print_cheat()
        elif len(args) > 2 and args[2].lower() in ("obj", "objectives"):
            p = os.path.join(bank_dir(args[1]), "objectives.md")
            if os.path.isfile(p):
                print(f"\n{CYN}{open(p, encoding='utf-8').read().rstrip()}{RST}\n")
            else:
                print(f"  {GRY}no objectives for {args[1]}{RST}")
        else:
            print_ref(args[1])
        sys.exit(0)

    # Title the tab only for an actual quiz run. Tool commands (sync/update/set/lint/...)
    # are often run inside another program's tab (e.g. a coding session hands over
    # `study sync` for the GPG prompt), and renaming that tab to "study" stuck there.
    set_title("study")
    pos, flags = parse_words(args)
    if pos:
        session, sel = pos[0], (pos[1].lower() if len(pos) > 1 else None)
    else:
        # menu pick may carry more words: '1 weak', '1 3 shuffle'
        session, extra = pick_session()
        if not session:
            return
        more_pos, more = parse_words(extra)
        flags = {k: flags[k] or more[k] for k in flags}
        sel = more_pos[0].lower() if more_pos else None

    set_title(f"study {session}")
    if session not in list_sessions():
        print(f"{RED}No session '{session}'. Available: "
              f"{', '.join(list_sessions()) or '(none)'}{RST}")
        return
    dispatch(session, sel, flags)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nbye")
