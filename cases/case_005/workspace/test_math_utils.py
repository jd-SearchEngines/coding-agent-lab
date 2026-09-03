import pytest

from math_utils import safe_divide


def test_safe_divide() -> None:
    assert safe_divide(6, 2) == 3


def test_safe_divide_has_domain_error() -> None:
    with pytest.raises(ValueError, match="zero denominator"):
        safe_divide(1, 0)

