#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """rct"""

    def __init__(self, width=0, height=0):
        """ao"""
        self.__width = width
        self.__height = height

    def __str__(self):
        """rq"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """rw"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """w"""
        return self.__width

    @width.setter
    def width(self, value):
        """w"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """h"""
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
        """cr"""
        return self.__width * self.__height

    def perimeter(self):
        """as"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
