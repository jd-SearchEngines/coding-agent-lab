# coding-agent-lab

`coding-agent-lab` is an evidence-first Season 1 project for understanding how
a tiny coding-agent loop grows into a production-oriented system. It is a
teaching and experiment repository, not a claim to outperform OpenHands or
SWE-agent.

## Upstream attribution

The baseline is informed by and intentionally kept compatible with the minimal
shape of [SWE-agent/mini-SWE-agent](https://github.com/SWE-agent/mini-swe-agent),
which is MIT licensed. The upstream repository is configured as the `upstream`
Git remote when the project is cloned from the maintained checkout. This
repository's code is newly written for the experiment unless a file says
otherwise; upstream code is not presented as original work.

## Run locally

```bash
python -m pip install -e '.[dev]'
python -m pytest
python scripts/run_experiments.py --versions minimal,explore,edit,verify,managed
```

The default experiment uses a deterministic local scripted model so it can be
reproduced without credentials. It is not LLM evidence. Provider-backed runs
are optional and must be recorded separately.

## Season 1 evidence

- [Experiment protocol](docs/EXPERIMENT_PROTOCOL.md)
- [Episode evidence](docs/content/GRAPHIC_SERIES_INDEX.md)
- [Season master report](reports/season1/MASTER_REPORT.md)
- [Video evidence pack](docs/content/VIDEO_MASTER_EVIDENCE.md)
- [ChatGPT handoff](docs/content/HANDOFF_TO_CHATGPT.md)

