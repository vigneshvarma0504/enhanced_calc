# Enhanced Calculator (Midterm Project)
# Project Description

The Enhanced Calculator is a modular, command-line Python application that performs a wide range of arithmetic operations and supports advanced features such as:

Power, Root, Modulus, Integer Division, Percentage, and Absolute Difference

Undo/Redo history using the Memento Design Pattern

Auto-save and logging via the Observer Design Pattern

Configurable settings loaded from a .env file

Continuous Integration (CI) via GitHub Actions

90 %+ automated test coverage enforced with pytest-cov

This project demonstrates software engineering principles like modular design, design patterns, and maintainability best practices.

# Installation Instructions
1. Clone the repository
git clone https://github.com/<your-username>/enhanced-calculator.git
cd enhanced-calculator

2. Create and activate a virtual environment
python -m venv venv
# On Windows PowerShell
.\venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate

3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Configuration Setup (.env)

Create a file named .env in the project root:

CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=50
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8


Then create the folders:

mkdir logs
mkdir history


These values control logging, history limits, auto-saving, and numerical precision.

# Usage Guide

Run the calculator REPL:

python app\calculator.py

Supported Commands
Command	Description
add a b	Add two numbers
subtract a b	Subtract second number from first
multiply a b	Multiply two numbers
divide a b	Divide first number by second (handles divide-by-zero)
power a b	Compute a raised to the power of b
root a b	Compute the b-th root of a
modulus a b	Compute the remainder of a ÷ b
int_divide a b	Integer division (floor division)
percent a b	Calculate (a / b) * 100
abs_diff a b	Absolute difference between numbers
history	Show all past calculations
help	Show all available commands
exit	Exit the program

Example session:

> add 5 3
Result: 8.0
> divide 10 0
Result: Error: Division by zero
> history
2025-11-03 15:10:21 | add(5, 3) = 8.0
> exit
Goodbye!

# Testing Instructions

Run all unit tests:

pytest


Run tests with coverage report:

pytest --cov=app --cov-report=term-missing


Typical output:

Name                      Stmts   Miss  Cover
----------------------------------------------
app/calculator.py            30      0   100%
app/operations.py             8      0   100%
app/history.py               18      0   100%
----------------------------------------------
TOTAL                       124      0   100%


All tests must pass with ≥ 90 % coverage (enforced by CI).

# CI/CD (GitHub Actions)

Continuous integration is handled by GitHub Actions.
Each push or pull request to main automatically:

Checks out the repository

Sets up Python 3.11

Installs dependencies from requirements.txt

Runs all tests with pytest-cov

Fails the build if coverage is below 90 %

Workflow file: .github/workflows/python-app.yml

# Logging

The app uses Python’s logging module.
Logs are stored in the directory defined by CALCULATOR_LOG_DIR in .env (default: logs/calculator.log).

Every calculation is logged in this format:

2025-11-03 15:23:45,612 - INFO - add(5, 3) = 8.0
