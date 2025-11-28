#!/usr/bin/env python3
"""salam"""

import csv
import json

class DictReader():
    """salam"""
    def convert_csv_to_json:
        """salam"""

    with open('input.csv', "r") as f:
        data = list(csv.DictReader(f))

    with open("data.json", "w") as f:
        json.dump(data, f)
