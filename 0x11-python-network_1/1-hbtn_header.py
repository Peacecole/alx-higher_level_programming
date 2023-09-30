#!/usr/bin/python3
"""
script that takes in and sends a request to given URL then displays
the value of the X-Request-Id variable found in the header of the
response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """takes in and sends a request to given URL then displays
    the value of the X-Request-Id variable found in the header
    of the response"""
    with urllib.request.urlopen(argv[1]) as response:
        html_id = response.info().get('X-Request-Id')
        print(html_id)
