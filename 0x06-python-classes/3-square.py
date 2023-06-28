#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """Represent the class Square"""

    def __init__(self, size=0):
        """Intializes a new attribute to the class Square

            Args:
                size (int): Integer value, the size of the new Square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
