from app.history import History
from app.calculation import Calculation

def test_add_and_clear_history():
    h = History()
    c = Calculation("add", 2, 3, 5)
    h.add(c)
    assert len(h.records) == 1
    h.clear()
    assert len(h.records) == 0
