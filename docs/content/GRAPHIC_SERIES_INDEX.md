# Graphic Series Index

| Episode | Project Version | Commit | Primary Case | Core Problem | Core Knowledge | Key Result | Key Bad Case | Final User Takeaway | Evidence Path |
|---|---|---|---|---|---|---|---|---|---|
| 1. 100行代码真的能做Coding Agent吗？ | v0.1-minimal | `5be3c77f` | case_001–005 | self-report is not proof | Minimal Agent Loop | 0/5 pass; 5 false finishes | all cases false-finish | a loop can act busy without solving | `docs/content/EP01/` |
| 2. 它为什么看不懂一个真实Repo？ | v0.2-explore | `73b464fb` | case_001–005 | missing context | Context Engineering | 5 exploration traces; 0/5 pass | explore then finish without edit | context selection is a capability | `docs/content/EP02/` |
| 3. 会改代码为什么不等于会修Bug？ | v0.3-edit | `6cc8e6be` | case_001–005 | wrong target/constraint risk | Action / Code Editing | 5/5 pass; 5 changed files | no in-loop test | patching existing code needs control | `docs/content/EP03/` |
| 4. Agent说修好了，你凭什么相信？ | v0.4-verify | `e4931bf0` | case_001–005 | completion claim lacks evidence | Verify | 5 recoveries; 5/5 pass | first patch fails pytest | tests, not claims, gate success | `docs/content/EP04/` |
| 5. 它开始执行Shell了，我敢把电脑交给它吗？ | v0.5-managed | `c089c029` | boundary probe | model intent vs permission | Execution Boundary | 5 denials; 5/5 pass | `/etc/passwd` denied | execution needs a boundary | `docs/content/EP05/` |
| 6. Agent失败以后为什么不能无脑Retry？ | v0.6-recovery | `e22bfa56` | failure/retry probe | repeated failure | State + Recovery | bounded retries; 5 recovery successes | budget exhaustion stops | failure must update state | `docs/content/EP06/` |
| 7. 怎么证明V2真的比V1好？ | v0.7-eval | `ac4a4e3e` | fixed dataset | no regression proof | Regression Eval | 5 versions compared | baseline 0/5 retained | compare on fixed cases | `docs/content/EP07/` |
| 8. 工业级Coding Agent到底多了什么？ | v1.0-final | `9676e70b` | fixed dataset | system capabilities/governance | capability map | 5/5 final pass; cost null | blocked/failed attempts retained | model loop is only the beginning | `docs/content/EP08/` |

All cases are synthetic local fixtures and are labeled as such. No row claims a
historical GitHub Issue reproduction.
