# app/exceptions.py

class CalculatorError(Exception):
    """Base class for calculator errors."""

class OperationError(CalculatorError):
    """Raised for invalid or failed operations."""

class ValidationError(CalculatorError):
    """Raised when user input is invalid."""
