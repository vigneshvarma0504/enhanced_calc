from app.operations import OperationFactory
import pytest

def test_add_operation():
    assert OperationFactory.perform("add", 5, 3) == 8

def test_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.perform("invalid_op", 1, 2)
