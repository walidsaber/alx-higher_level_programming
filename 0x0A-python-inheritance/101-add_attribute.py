#!/usr/bin/python3
"""adding ATT"""


def add_attribute(obj, att, value):
    """adding att"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
