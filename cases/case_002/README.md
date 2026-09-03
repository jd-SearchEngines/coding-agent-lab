# case_002 — parse a bounded port

- `case_type`: synthetic
- `source_repo`: local teaching fixture
- `issue_url`: null
- `base_commit`: repository commit containing this fixture
- `license`: MIT (this repository)
- `expected_behavior`: accept integer ports from 1 through 65535 and reject other input
- `verification`: `pytest -q`

