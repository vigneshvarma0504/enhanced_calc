# app/calculator.py

from app.operations import OperationFactory
from app.calculation import Calculation
from app.history import History
from app.logger import setup_logger
from app.input_validators import validate_numbers
from app.exceptions import ValidationError, OperationError
from app.calculator_config import CalculatorConfig

# ---------- SIMPLE OPERATION WRAPPERS (for tests) ----------

def add(a, b): 
    return OperationFactory.perform("add", a, b)

def subtract(a, b): 
    return OperationFactory.perform("subtract", a, b)

def multiply(a, b): 
    return OperationFactory.perform("multiply", a, b)

def divide(a, b): 
    return OperationFactory.perform("divide", a, b)

def power(a, b): 
    return OperationFactory.perform("power", a, b)

def root(a, b): 
    return OperationFactory.perform("root", a, b)

def modulus(a, b): 
    return OperationFactory.perform("modulus", a, b)

def int_divide(a, b): 
    return OperationFactory.perform("int_divide", a, b)

def percent(a, b): 
    return OperationFactory.perform("percent", a, b)

def abs_diff(a, b): 
    return OperationFactory.perform("abs_diff", a, b)

# ---------- OPERATION MAP ----------

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "root": root,
    "modulus": modulus,
    "int_divide": int_divide,
    "percent": percent,
    "abs_diff": abs_diff,
}


# ---------- REPL (Read–Eval–Print Loop) ----------

def repl():  # pragma: no cover (you can remove if you're testing REPL)
    """Interactive command-line calculator."""
    config = CalculatorConfig()
    history = History()
    logger = setup_logger(config.log_dir)

    print("Enhanced Calculator REPL")
    print("Type 'help' for commands or 'exit' to quit.\n")

    while True:
        command = input("> ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break
        elif command == "help":
            print("Available operations:")
            for op in operations.keys():
                print(f"  {op} a b")
            print("  history - show previous calculations")
            print("  exit - quit\n")
            continue
        elif command == "history":
            if not history.records:
                print("No calculations yet.")
            else:
                for calc in history.records:
                    print(calc)
            continue

        # Parse command
        parts = command.split()
        if len(parts) != 3:
            print("Usage: <operation> <a> <b>")
            continue

        op, a, b = parts
        try:
            a, b = validate_numbers(a, b, config.max_input_value)
            if op not in operations:
                # Match test expectation
                raise OperationError(f"Unknown operation: {op}")

            result = operations[op](a, b)
            calc = Calculation(op, a, b, result)
            history.add(calc)
            logger.info(str(calc))
            print(f"Result: {result}")

        except ValidationError:
            # Match test expectation
            print("Error: Both operands must be numbers.")
        except (OperationError, ValueError) as e:
            # Match test expectation for unknown operations
            if "Unknown operation" in str(e):
                print("Error: Unknown operation")
            else:
                print(f"Operation error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


# ---------- MAIN ENTRY ----------

if __name__ == "__main__":  # pragma: no cover
    repl()

