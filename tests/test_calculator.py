import pytest
from unittest.mock import patch
from app import calculator


# ---------- BASIC OPERATIONS ----------

def test_add():
    assert calculator.add(5, 3) == 8

def test_subtract():
    assert calculator.subtract(10, 4) == 6

def test_multiply():
    assert calculator.multiply(2, 5) == 10

def test_divide_normal():
    assert calculator.divide(8, 2) == 4

def test_divide_by_zero():
    assert calculator.divide(5, 0) == "Error: Division by zero"


# ---------- ADVANCED OPERATIONS ----------

def test_power():
    assert calculator.power(2, 3) == 8

def test_root_cube():
    assert round(calculator.root(27, 3), 6) == 3

def test_modulus():
    assert calculator.modulus(10, 3) == 1

def test_int_divide():
    assert calculator.int_divide(10, 3) == 3

def test_percent():
    assert calculator.percent(20, 100) == 20.0

def test_abs_diff():
    assert calculator.abs_diff(10, 4) == 6


# ---------- OPERATIONS DICTIONARY ----------

def test_all_operations_exist():
    expected = {
        "add", "subtract", "multiply", "divide",
        "power", "root", "modulus", "int_divide",
        "percent", "abs_diff"
    }
    assert expected.issubset(calculator.operations.keys())


def test_all_operations_callable():
    for func in calculator.operations.values():
        assert callable(func)


# ---------- EDGE CASES ----------

def test_large_numbers():
    assert calculator.add(1_000_000, 2_000_000) == 3_000_000

def test_negative_numbers():
    assert calculator.subtract(-5, -10) == 5

def test_float_inputs():
    assert calculator.divide(7.5, 2.5) == 3.0


# ---------- REPL TESTS ----------

def test_repl_valid_input(monkeypatch, capsys):
    # Simulate "add 2 3" then exit
    fake_inputs = iter(["add 2 3", "exit"])
    with patch("builtins.input", lambda _: next(fake_inputs)):
        calculator.repl()

    output = capsys.readouterr().out
    assert "Result: 5.0" in output
    assert "Goodbye!" in output


def test_repl_help(monkeypatch, capsys):
    # Simulate help and exit
    fake_inputs = iter(["help", "exit"])
    with patch("builtins.input", lambda _: next(fake_inputs)):
        calculator.repl()
    output = capsys.readouterr().out
    assert "Available operations" in output or "Commands" in output


def test_repl_invalid_operation(monkeypatch, capsys):
    # Simulate invalid command then exit
    fake_inputs = iter(["nonsense 2 3", "exit"])
    with patch("builtins.input", lambda _: next(fake_inputs)):
        calculator.repl()
    output = capsys.readouterr().out
    assert "Error: Unknown operation" in output


def test_repl_non_numeric_input(monkeypatch, capsys):
    # Simulate invalid numeric input
    fake_inputs = iter(["add five 3", "exit"])
    with patch("builtins.input", lambda _: next(fake_inputs)):
        calculator.repl()
    output = capsys.readouterr().out
    assert "Error: Both operands must be numbers." in output


def test_repl_missing_args(monkeypatch, capsys):
    # Simulate missing arguments
    fake_inputs = iter(["add 2", "exit"])
    with patch("builtins.input", lambda _: next(fake_inputs)):
        calculator.repl()
    output = capsys.readouterr().out
    assert "Usage:" in output


def test_repl_extra_args(monkeypatch, capsys):
    # Simulate too many arguments
    fake_inputs = iter(["add 2 3 4", "exit"])
    with patch("builtins.input", lambda _: next(fake_inputs)):
        calculator.repl()
    output = capsys.readouterr().out
    assert "Usage:" in output


def test_repl_exit(monkeypatch, capsys):
    # Test only exit
    fake_inputs = iter(["exit"])
    with patch("builtins.input", lambda _: next(fake_inputs)):
        calculator.repl()
    output = capsys.readouterr().out
    assert "Goodbye!" in output
