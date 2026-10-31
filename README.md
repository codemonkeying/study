# study

A terminal quiz engine for cert study. Comes with a Network+ (N10-009) bank; add your own. Your progress syncs across machines (phone included, via Termux) through a git repo you choose: GitHub, Gitea, anything.

## Install

Needs Python 3.8+ and git (Linux, macOS, Termux).

```sh
git clone https://github.com/codemonkeying/study.git ~/study && ~/study/install.sh
study init                       # new local data repo
# install.sh links into ~/.local/bin; make sure that's on your PATH
study init git@host:you/data.git # or clone your existing one
```

Banks ship with the engine (`banks/`). Your data repo holds your results, synced per device, plus any private banks of your own (same name = yours wins). Point every device at the same data remote, any private git repo, to share progress.

```toml
# ~/.config/study/config.toml
data = "~/.local/share/study"   # your data repo (results + private banks)
auto_update = true              # engine checks for updates once a day
```

`study update` pulls the engine and your data now. Env overrides: `STUDY_DATA` (data dir), `STUDY_NO_UPDATE=1`, `QUIZ_DEVICE` (device name in results files).

## Use

```sh
study                    # menu
study netplus 3          # run test 3
study mybank weak        # drill weak spots until cleared
study mybank new         # unseen questions only
study mybank practice_exam   # timed, domain-weighted mock (needs exam.json)
study subnet             # subnetting drill (hard, history)
study ref mybank         # print the bank's ref.md
study flags              # questions you flagged with /flag
study build mybank       # compile drafts into tests.md, then lint
study sync               # push your results + bank changes (if lint passes), pull the rest
study update             # pull engine + data
study --lint             # check every bank
```

## Banks

Included: `netplus` (907 questions incl. PBQs, timed mock, subnet drill).

Your own go in `banks/<name>/` in your data repo:

| File | |
|---|---|
| `drafts/*.txt` | what you write; `study build <name>` compiles them to `tests.md` |
| `tests.md` | the bank the quiz reads |
| `exam.json` | optional mock exam: `{"n": 90, "mins": 90, "pass": 720, "pbq": 6, "weights": {"1": 23, "2": 20}, "subnet_drill": "basic"}` (`subnet_drill` alone is fine too: adds the drill to the bank menu) |
| `ref.md` | optional quick reference (`study ref <name>`) |
| `acronyms.md` | optional; acronyms get expanded in explanations |

Draft format:

```
## Test 1 - Ports

Which port does SSH use?
+ 22
- 23
- 443
* SSH = 22, Telnet = 23.
@ 1.4.ports

Type the HTTPS port.
= 443

Pick the protocol for each port.
p 53 :: A DNS · B DHCP · C NTP = a
p 123 :: A DNS · B DHCP · C NTP = c
```

`+`/`-` options, `=` typed answer, `p` multi-part, `*` explanation, `@` objective tag (first character is the exam domain), `!` key fact. Results are per device (`results/<bank>@<host>.json`), so syncing never conflicts.

## Disclaimer

The included banks are original questions written against publicly available exam objectives. They contain no real exam content and are not affiliated with or endorsed by any certification vendor.

## License

Copyright (c) 2026 codemonkeying. All rights reserved.
