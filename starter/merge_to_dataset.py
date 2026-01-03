#!/usr/bin/env python3

import json
import os
import pandas as pd
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

    The log format should be:
    YYYY-MM-DDTHH:MM:SSZ - merge_to_dataset.py: <message>
    """
    # TODO:
    # 1. Generate a UTC timestamp
    # 2. Open LOG_FILE in append mode
    # 3. Write the formatted log message
    pass
# -----------------------------

CLEAN_DIR = "clean"
DATASET_DIR = "dataset"
OUTPUT_FILE = os.path.join(DATASET_DIR, "clean_products.csv")

# Create dataset directory if it doesn't exist
os.makedirs(DATASET_DIR, exist_ok=True)

rows = []

# TODO:
# Write a log entry indicating that dataset merging has started.
#
# log("Starting dataset merge")

for filename in os.listdir(CLEAN_DIR):
    if not filename.endswith(".json"):
        continue

    file_path = os.path.join(CLEAN_DIR, filename)

    try:
        # TODO:
        # Open the JSON file and load its contents
        # Append the loaded dictionary to the `rows` list
        


        # TODO:
        # Write a log entry indicating the file was successfully loaded.
        

        pass
    except Exception as e:
        # TODO:
        # Write a log entry indicating the file failed to load.
        #
        pass

# TODO:
# If no rows were loaded, log a message and exit the script with a non-zero status.
#

# ---------- pandas aggregation ----------

# TODO:
# Create a pandas DataFrame from the `rows` list.
#
# df = ...

# TODO:
# Perform very light cleanup:
# - Ensure `price` is a float
# - Ensure `stock` is an integer (fill missing values with 0)
#
# df["price"] = ...
# df["stock"] = ...

# TODO:
# Write the DataFrame to OUTPUT_FILE as a CSV file.
# Do not include the index.

# TODO:
# Write a log entry indicating that the dataset was written successfully.

# TODO:
# Write a log entry indicating that the merge process is complete.
#