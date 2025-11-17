#!/usr/bin/python3
import sys


if __name__ == "__main__":
    argv = sys.argv[1:]
    cem = 0

    for arg in argv:
        cem += int(arg)

    print(cem)
