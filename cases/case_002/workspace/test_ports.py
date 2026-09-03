import pytest

from ports import parse_port


def test_parse_port_accepts_valid_port() -> None:
    assert parse_port("443") == 443


@pytest.mark.parametrize("value", ["0", "65536", "http"])
def test_parse_port_rejects_invalid_port(value: str) -> None:
    with pytest.raises(ValueError):
        parse_port(value)

