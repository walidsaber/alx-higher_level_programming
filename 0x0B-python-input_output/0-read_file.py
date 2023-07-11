#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """Reads a text"""
    with open(filename, 'r') as f:
        print(f.read(), end='')
