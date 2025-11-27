#!/usr/bin/python3
""" salam """


class BaseGeometry():
    """ salam """
    def area(self):
        """ salam """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ salam """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
