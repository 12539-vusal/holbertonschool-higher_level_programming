#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    count = len(argv)

    cem = 0
    if count == 0:
        print(cem)
    else:
        for arg in argv:
            cem += int(arg)
    print(cem)
