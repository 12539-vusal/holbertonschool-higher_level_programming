#!/usr/bin/python3
"""MyList class"""

class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Sort the list in-place and print"""
        self.sort()
        print(self)
