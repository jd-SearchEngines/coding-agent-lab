# case_003 — truncate text without splitting a word

- `case_type`: synthetic
- `source_repo`: local teaching fixture
- `issue_url`: null
- `base_commit`: repository commit containing this fixture
- `license`: MIT (this repository)
- `expected_behavior`: return text no longer than the requested limit and append an ellipsis only when truncated
- `verification`: `pytest -q`

