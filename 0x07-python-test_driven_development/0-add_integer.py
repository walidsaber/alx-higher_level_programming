#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """sum of two ints or floats

    Args:
        a: first val
        b: second val

    Raises:
        TypeError: if either a or b are not float or int

    Returns:
        a + b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
