#!/usr/bin/python3
"""Defines function that appends a string at the end of a text file"""
import json


def to_json_string(my_obj):
    """Returns the number of characters added"""
    return json.dumps(my_obj)
