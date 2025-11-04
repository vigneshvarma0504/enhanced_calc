# tests/test_history_csv.py
import os
import pandas as pd
from app.history import History
from app.calculation import Calculation

def test_save_and_load_history(tmp_path):
    filename = tmp_path / "history.csv"
    h1 = History()
    h1.add(Calculation("add", 2, 3, 5))
    h1.add(Calculation("multiply", 4, 5, 20))

    h1.save_to_csv(filename)
    assert os.path.exists(filename)

    h2 = History()
    h2.load_from_csv(filename)
    assert len(h2.records) == 2
    assert isinstance(h2.records[0], Calculation)
