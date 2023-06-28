#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents the class Square"""

    def __init__(self, size=0):
        """Intializes a new attribute to the class Square

            Args:
                size (int): Integer value, the size of the new Square"""

        self.size = size

    @property
    def size(self):
        """Sets the current size of the class Square to private"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the class Square"""
        return (self.__size * self.__size)
