#!/usr/bin/python3
"""
Base geo
"""


class BaseGeometry:
    """Class"""
    def area(self):
        """raising exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """is greater?"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
