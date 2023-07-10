#!/usr/bin/python3
"""Class"""


class MyInt(int):
    """invertation"""

    def __eq__(self, value):
        """xa"""
        return self.real != value

    def __ne__(self, value):
        """xb"""
        return self.real == value
