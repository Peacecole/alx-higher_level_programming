#!/usr/bin/python3
"""Object attribute lookup function."""


def lookup(obj):
    """Returns available attributes in an object"""
    return (dir(obj))
