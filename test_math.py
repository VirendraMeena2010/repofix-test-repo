from math_utils import add, divide, is_even
import pytest


def test_add():
    assert add(2, 3) == 5   # ❌ will fail


def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Error"   # ❌ will crash currently


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False   # ❌ will fail
