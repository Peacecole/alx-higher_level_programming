#!/usr/bin/python3
"""
takes in and sends a request to a given URL then displays the
value of the X-Request-Id variable found in the header of the
response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """takes in and sends a request to a given URL then displays
    the value of the X-Request-Id variable found in the header
    of the response using requests"""
    r = requests.get(argv[1])
    try:
        r_id = r.headers['X-Request-Id']
        print(r_id)
    except:
        pass
