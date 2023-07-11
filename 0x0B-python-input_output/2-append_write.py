#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """append a text"""
    with open(filename, 'a') as f:
        return f.write(text)
