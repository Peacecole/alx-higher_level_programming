#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status using requests"""
import requests


if __name__ == "__main__":
    """fetche https://intranet.hbtn.io/status using requests"""
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
