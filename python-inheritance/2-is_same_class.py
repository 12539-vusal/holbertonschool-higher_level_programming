#!/usr/bin/python3
""" SALAM """

def is_same_class(obj, a_class):
    """ Check if obj is an instance of a_class, including subclasses """
    return isinstance(obj, a_class) and type(obj) == a_class
