#!/usr/bin/python3
"""salam"""


def read_file(filename=""):
    """salam"""
    with open(filename, encoding="utf-8") as f:
        for line in f.read():
            print(line, end="")
