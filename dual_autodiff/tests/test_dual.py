import pytest
from sub_dual_autodiff import Dual

def test_dual_initialization():
    d = Dual(3, 2)
    assert d.real == 3
    assert d.dual == 2

def test_dual_repr():
    d = Dual(3, 2)
    assert repr(d) == "Dual(real=3, dual=2)"
