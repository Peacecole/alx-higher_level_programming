#!/usr/bin/python3
"""Defines a BaseGeometry based on 5-base_geometry.py"""


class BaseGeometry:
    """Represent BaseGeometry"""

    def area(self):
        """If not implemented."""
        raise Exception("area() is not implemented")
