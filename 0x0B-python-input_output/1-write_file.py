#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """write text"""
    with open(filename, 'w') as f:
        return f.write(text)
