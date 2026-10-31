#!/usr/bin/env python3
"""study build BANK: compile banks/BANK/drafts/*.txt into banks/BANK/tests.md.

Draft format, one block per question, blank line between:
   ## Test N - Title           test header (N is renumbered, count appended)
   Question text               stem (first line)
   + right / - wrong           multiple choice options
   = answer | alt              typed answer
   p prompt :: A x · B y = a   multi-part question, one part per line
   * note                      explanation shown after answering
   @ 1.4.tag                   objective tag (first char = exam domain)
   ! fact                      key fact for the current test
Stems and notes can't contain [ or ].

Stats move with reworded questions when a test keeps its length."""
import json, os, re, sys
def render(src):
    out, facts, n, q = [], [], 0, None
    def flush():
        nonlocal q, n
        if not q: return
        n += 1; ind = " " * (3 if n < 10 else 4)
        out.append(f"{n}. {q['stem']}")
        if q["parts"]: out.extend(f"{ind}- [p] {x}" for x in q["parts"])
        elif q["typed"]: out.append(f"{ind}- [=] {q['typed']}")
        else: out.append(ind + "  ".join(("- **[x] %s**" if c else "- [ ] %s") % t for c, t in q["opts"]))
        out.append(f"{ind}- *{q['note']}*")
        if q["tag"]: out.append(f"{ind}- @{q['tag']}")
        for k in ("stem", "note"):
            assert "[" not in q[k] and "]" not in q[k], (n, q[k])
        q = None
    def endtest():
        nonlocal facts
        flush()
        if facts:
            out.append(""); out.append("### Key facts")
            out.extend(f"- **{f}**" for f in facts)
        facts = []
    hdr = None
    for raw in src.splitlines():
        l = raw.rstrip()
        if l.startswith("## Test "):
            endtest()
            if hdr is not None: out[hdr] += f" ({n} Q)"
            out.append(""); out.append(l); hdr = len(out) - 1; out.append(""); n = 0; continue
        if not l.strip(): flush(); continue
        if l.startswith("! "): flush(); facts.append(l[2:]); continue
        if q is None:
            q = {"stem": l.strip(), "opts": [], "typed": "", "note": "", "tag": "", "parts": []}; continue
        k, v = l[:2], l[2:].strip()
        if k == "+ ": q["opts"].append((True, v))
        elif k == "- ": q["opts"].append((False, v))
        elif k == "= ": q["typed"] = v
        elif k == "p ": q["parts"].append(v)
        elif k == "* ": q["note"] = (q["note"] + " " + v).strip()
        elif k == "@ ": q["tag"] = v
        else: q["stem"] += " " + l.strip()
    endtest()
    if hdr is not None: out[hdr] += f" ({n} Q)"
    return "\n".join(out).strip() + "\n"


def build(bank, data, d=None):
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))
    import study
    d = d or os.path.join(data, "banks", bank)
    if not os.path.isdir(os.path.join(d, "drafts")):
        sys.exit(f"no drafts dir: {d}/drafts")
    files = sorted(f for f in os.listdir(os.path.join(d, "drafts")) if f.endswith(".txt"))
    src = "\n".join(open(os.path.join(d, "drafts", f), encoding="utf-8").read().rstrip() + "\n" for f in files)
    n = [0]
    def hdr(m):
        n[0] += 1
        return f"## Test {n[0]} - {m.group(1)}"
    src = re.sub(r"^## Test \d+ - (.*)$", hdr, src, flags=re.M)
    path = os.path.join(d, "tests.md")
    old = study.parse_bank(path) if os.path.exists(path) else {}
    try:
        out = render(src)
    except AssertionError as e:
        sys.exit(f"build failed, tests.md untouched: {e}")
    tmp = path + ".tmp"
    open(tmp, "w", encoding="utf-8").write(out)
    os.replace(tmp, path)
    new = study.parse_bank(path)
    remap = {}
    for t in old:
        a, b = old[t]["questions"], new.get(t, {}).get("questions", [])
        if len(a) != len(b):
            continue
        ida = [study.qid(t, q) for q in a]
        idb = [study.qid(t, q) for q in b]
        for ia, ib, qb in zip(ida, idb, b):
            # only a reworded question in place: old id gone, new id not already present
            if ia != ib and ia not in idb and ib not in ida:
                remap[ia] = (ib, qb["q"])
    res = os.path.join(data, "results")
    for f in sorted(os.listdir(res)) if os.path.isdir(res) else []:
        if not f.startswith(bank + "@"):
            continue
        p = os.path.join(res, f); j = json.load(open(p)); q = j["questions"]; m = 0
        for k, (nk, txt) in remap.items():
            if k in q:
                st = q.pop(k); st["q"] = txt; m += 1
                if nk in q: study._merge_stat(q[nk], st)
                else: q[nk] = st
        if m:
            study._atomic_write_json(p, j)
    print(f"{bank}: {n[0]} tests, {len(remap)} reworded questions kept their stats")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        sys.exit("usage: build.py BANK DATA_DIR [BANK_DIR]")
    build(*sys.argv[1:])
