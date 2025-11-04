# app/operations.py

import math

class OperationFactory:
    """Factory to create and perform mathematical operations."""

    @staticmethod
    def perform(operation, a, b):
        operations = {
            "add": lambda a, b: a + b,
            "subtract": lambda a, b: a - b,
            "multiply": lambda a, b: a * b,
            "divide": lambda a, b: a / b if b != 0 else "Error: Division by zero",
            "power": lambda a, b: a ** b,
            "root": lambda a, b: a ** (1 / b),
            "modulus": lambda a, b: a % b,
            "int_divide": lambda a, b: a // b,
            "percent": lambda a, b: (a / b) * 100,
            "abs_diff": lambda a, b: abs(a - b),
        }

        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")

        return operations[operation](a, b)
