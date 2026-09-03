# Handoff to ChatGPT

## Repository

- GitHub: `https://github.com/jd-SearchEngines/coding-agent-lab`
- Main branch: `main`
- Upstream: `https://github.com/SWE-agent/mini-swe-agent`
- Upstream inspected commit: `04d809ceab9df28f9adaed044884180159172930`

## Season status

Season 1 engineering path EP01–EP08 is implemented and independently
committed. Final local status is intended to be a clean `main` checkout after
the publication commit.

## Commit map

| Stage | Commit |
|---|---|
| Baseline experiment | `5be3c77f0246ff206c01e7302aa6e3675f924901` |
| EP01 | `5be3c77f0246ff206c01e7302aa6e3675f924901` |
| EP02 | `73b464fb60b23b97b3dc5bb455292ba3e1c2d8b6` |
| EP03 | `6cc8e6be10313b180e8caf321fb15e99268319b8` |
| EP04 final corrected evidence | `e4931bf0daa1401bebf91a23534ba44bcc577b8d` |
| EP05 | `c089c029c2713a5ab0b47483dd5f9758ac13aea8` |
| EP06 | `e22bfa56c52858494a7c1c52b858d2b03c2977d5` |
| EP07 | `ac4a4e3ebf4922793d7cbd5f01fea4b4cfa6e771` |
| EP08 final benchmark | `f71c2a9f1e251cb964965a352b04e869a190e94c` |

The earlier EP04 feature commit `1b61b9dc6a7e72cd3c62a8114a43f770008a5ad0`
contains the first 4/5 run; `e4931bf0...` contains the corrected reproducible
run after fixing interpreter bytecode cache behavior.

## Evidence paths

- Episode packs: `docs/content/EP01/` through `docs/content/EP08/`
- Machine-readable evidence: each episode's `evidence.json`
- Master report: `reports/season1/MASTER_REPORT.md`
- Metrics: `reports/season1/metrics_summary.csv`
- Failure taxonomy: `reports/season1/failure_taxonomy.md`
- Eval config and harness: `evals/configs/season1.json`, `scripts/run_season1_eval.py`
- Final architecture: `docs/architecture/final-capability-map.mmd`
- Video pack: `docs/content/VIDEO_MASTER_EVIDENCE.md`

## Known blocked experiments

Provider-backed LLM runs are `BLOCKED_BY_MODEL_RUNTIME`: no model credentials
were available. The public historical GitHub Issue corpus is also not
completed; all five current cases are synthetic and labeled as such.

## Claims policy

Real deterministic run facts are the persisted JSONL/CSV values: 5 fixed cases,
baseline 0/5 with 5 false finishes, final 5/5 with 0 false finishes, 5
permission denials, 10 failed tool actions, and cost `null`. Inferences are
limited to the engineering lesson that verification, permissions, state, and
regression make failure observable and bounded. No provider-model quality,
production safety, public-Issue coverage, or cost claim is supported.

> When producing the eight articles or the video, use only the real Repo, Run,
> and Report evidence above. Do not invent results for content effect.
