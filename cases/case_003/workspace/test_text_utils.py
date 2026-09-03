from text_utils import truncate_text


def test_truncate_text_keeps_words_and_limit() -> None:
    assert truncate_text("coding agent", 9) == "coding..."
    assert len(truncate_text("coding agent", 9)) <= 9
