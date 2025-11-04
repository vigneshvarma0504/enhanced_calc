# tests/test_calculation_str.py
from app.calculation import Calculation

def test_str_and_to_dict_methods():
    c = Calculation("add", 1, 2, 3)
    s = str(c)
    d = c.to_dict()
    assert "add" in s
    assert "result" in d
