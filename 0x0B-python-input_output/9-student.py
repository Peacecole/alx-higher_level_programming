#!/usr/bin/python3
"""Defines a class Student that defines a student"""


class Student:
    """Represent an object student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new object Student.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the object Student."""
        return self.__dict__
