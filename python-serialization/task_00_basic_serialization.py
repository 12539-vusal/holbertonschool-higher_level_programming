#!/usr/bin/python3
"""salam"""

import json


def serialize_and_save_to_file(data, filename):
    """salam"""
    with open(filename, "w", enconding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """salam"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
