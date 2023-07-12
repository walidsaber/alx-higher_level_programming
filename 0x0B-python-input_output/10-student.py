#!/usr/bin/python3
"""Student r"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """start"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """dic student"""

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
