import pytest
from sub_dual_autodiff import Dual

def test_dual_addition():
    d1 = Dual(3, 2)
    d2 = Dual(1, 1)
    result = d1 + d2
    assert result.real == 4
    assert result.dual == 3

def test_dual_subtraction():
    d1 = Dual(3, 2)
    d2 = Dual(1, 1)
    result = d1 - d2
    assert result.real == 2
    assert result.dual == 1

def test_dual_multiplication():
    d1 = Dual(3, 2)
    d2 = Dual(1, 1)
    result = d1 * d2
    assert result.real == 3
    assert result.dual == 5

def test_dual_division():
    d1 = Dual(4, 2)
    d2 = Dual(2, 1)
    result = d1 / d2
    assert result.real == 2
    assert result.dual == 0
