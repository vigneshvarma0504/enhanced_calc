# app/input_validators.py

from app.exceptions import ValidationError

def validate_numbers(a, b, max_value=1_000_000):
    """Ensure a and b are numbers within allowed range."""
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValidationError("Inputs must be numeric.")
    if abs(a) > max_value or abs(b) > max_value:
        raise ValidationError("Input value exceeds limit.")
    return a, b
