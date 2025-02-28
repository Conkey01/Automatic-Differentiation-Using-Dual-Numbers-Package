import pytest
import math
from sub_dual_autodiff import Dual

def test_dual_sin():
    d = Dual(0, 1)
    result = d.sin()
    assert math.isclose(result.real, 0.0, rel_tol=1e-9)
    assert math.isclose(result.dual, 1.0, rel_tol=1e-9)

def test_dual_cos():
    d = Dual(0, 1)
    result = d.cos()
    assert math.isclose(result.real, 1.0, rel_tol=1e-9)
    assert math.isclose(result.dual, 0.0, rel_tol=1e-9)
    
def test_dual_tan():
    d = Dual(0, 1)
    result = d.tan()  
    assert math.isclose(result.real, 0.0, rel_tol=1e-9)
    assert math.isclose(result.dual, 1.0, rel_tol=1e-9)

def test_dual_log():
    d = Dual(math.e, 1)
    result = d.log()
    assert math.isclose(result.real, 1.0, rel_tol=1e-9)
    assert math.isclose(result.dual, 1 / math.e, rel_tol=1e-9)

def test_dual_exp():
    d = Dual(1, 1)
    result = d.exp()
    assert math.isclose(result.real, math.exp(1), rel_tol=1e-9)
    assert math.isclose(result.dual, math.exp(1), rel_tol=1e-9)
