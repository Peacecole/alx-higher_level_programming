#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with functionality as != """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with functionality as == """
        return self.real == value
