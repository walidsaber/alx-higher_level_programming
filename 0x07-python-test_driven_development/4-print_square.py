#!/usr/bin/python3
""" sqr """


def print_square(size):
    """ orubt """

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is not int:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print("")
