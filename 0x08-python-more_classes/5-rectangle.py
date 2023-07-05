#!/usr/bin/python3
"""rec"""


class Rectangle:
    """rec"""

    def __init__(self, width=0, height=0):
        """q"""
        self.__width = width
        self.__height = height

    def __str__(self):
        """r"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """h"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ del msg"""
        print("Bye rectangle...")

    @property
    def width(self):
        """width """
        return self.__width

    @width.setter
    def width(self, value):
        """width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """hh"""
        return self.__height

    @height.setter
    def height(self, value):
        """h"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """rc"""
        return self.__width * self.__height

    def perimeter(self):
        """rt"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
