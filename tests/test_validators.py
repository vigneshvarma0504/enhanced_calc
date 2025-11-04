import pytest
from app.input_validators import validate_numbers
from app.exceptions import ValidationError

def test_valid_numbers():
    a, b = validate_numbers("3", "4")
    assert a == 3.0 and b == 4.0

def test_invalid_numbers():
    with pytest.raises(ValidationError):
        validate_numbers("x", "4")

def test_exceeds_max_value():
    with pytest.raises(ValidationError):
        validate_numbers("100000000", "1", 10_000)
