# app/calculation.py
from datetime import datetime

class Calculation:
    """Represents a single calculation instance."""

    def __init__(self, operation_name, a, b, result):
        self.operation_name = operation_name
        self.a = a
        self.b = b
        self.result = result
        self.timestamp = datetime.now()

    def to_dict(self):
        """Return calculation details as a dictionary."""
        return {
            "operation": self.operation_name,
            "a": self.a,
            "b": self.b,
            "result": self.result,
            "timestamp": self.timestamp.isoformat()
        }

    def __str__(self):  # pragma: no cover
        return f"{self.timestamp:%Y-%m-%d %H:%M:%S} | {self.operation_name}({self.a}, {self.b}) = {self.result}"
