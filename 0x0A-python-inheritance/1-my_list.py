#!/usr/bin/python3
"""Defines a class that inherits from a list"""


class MyList(list):
    """Prints sorted printing for the built-in list class."""

    def print_sorted(self):
        print(sorted(self))
