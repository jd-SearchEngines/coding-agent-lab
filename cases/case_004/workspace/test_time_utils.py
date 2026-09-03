import pytest

from time_utils import format_seconds


def test_format_seconds_zero_pads() -> None:
    assert format_seconds(65) == "01:05"


def test_format_seconds_rejects_negative() -> None:
    with pytest.raises(ValueError):
        format_seconds(-1)

