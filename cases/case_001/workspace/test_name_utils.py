from name_utils import normalize_name


def test_normalize_name_collapses_whitespace() -> None:
    assert normalize_name("  Ada   Lovelace ") == "ada lovelace"

