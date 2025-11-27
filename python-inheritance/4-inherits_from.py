#!/usr/bin/python3
""" SALAM """


def inherits_from(obj, a_class):
    """ SALAM """
    if issubclass(obj) and isinstance(obj, a_class):
        return True
    else:
        return False
