#!/usr/bin/python3
"""subCLASS"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """SQUARE"""

    def __init__(self, size):
        """Initializing"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
