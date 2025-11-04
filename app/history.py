# app/history.py

import pandas as pd
from app.calculation import Calculation

class History:
    """Manages calculator history list and persistence."""

    def __init__(self):
        self.records = []

    def add(self, calculation: Calculation):
        self.records.append(calculation)

    def clear(self):
        self.records.clear()

    def to_dataframe(self):
        data = [c.to_dict() for c in self.records]
        return pd.DataFrame(data)

    def save_to_csv(self, filename):
        df = self.to_dataframe()
        df.to_csv(filename, index=False)

    def load_from_csv(self, filename):
        df = pd.read_csv(filename)
        self.records = [
            Calculation(row['operation'], row['a'], row['b'], row['result'])
            for _, row in df.iterrows()
        ]
