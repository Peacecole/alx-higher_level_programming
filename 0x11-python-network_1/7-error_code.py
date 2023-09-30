#!/usr/bin/python3
"""
takes in, sends a request to a given URL then displays the
body of the response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in, sends a request to a given URL then displays the
    body of the response using requests
    """
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
