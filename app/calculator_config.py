# app/calculator_config.py

import os
from dotenv import load_dotenv

class CalculatorConfig:
    """Loads calculator configuration from .env file."""

    def __init__(self):
        load_dotenv()
        self.log_dir = os.getenv("CALCULATOR_LOG_DIR", "logs")
        self.history_dir = os.getenv("CALCULATOR_HISTORY_DIR", "history")
        self.max_history = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 50))
        self.auto_save = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
        self.precision = int(os.getenv("CALCULATOR_PRECISION", 2))
        self.max_input_value = int(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1_000_000))
        self.encoding = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
