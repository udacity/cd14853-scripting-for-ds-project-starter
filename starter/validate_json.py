#!/usr/bin/env python3

import json
import sys
import os
import datetime

# ---------- logging ----------
LOGS_DIR = "logs"
TODAY = datetime.datetime.utcnow().strftime("%Y-%m-%d")
LOG_FILE = os.path.join(LOGS_DIR, f"{TODAY}.log")
os.makedirs(LOGS_DIR, exist_ok=True)

def log(message):
    """
    TODO:
    Implement this function to write a timestamped log message
    to the daily log file.

    Format:
    YYYY-MM-DDTHH:MM:SSZ - validate_json.py: <message>
    """
    # TODO:
    # 1. Generate a UTC timestamp
    # 2. Open LOG_FILE in append mode
    # 3. Write the formatted log message
    pass
# -----------------------------

# TODO:
# Check that exactly one command-line argument was provided.
# If not:
# - Write a log entry
# - Exit the script with a non-zero status

# TODO:
# Extract the file path from sys.argv.

# TODO:
# Check if the file is empty.
# If it is:
# - Write a log entry
# - Exit the script with a non-zero status

# TODO:
# Load the JSON file.
# If parsing fails:
# - Write a log entry
# - Exit the script with a non-zero status
