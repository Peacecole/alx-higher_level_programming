#!/usr/bin/python3
"""
takes in a URL, an email and sends a POST request to the passed URL
with the email as a parameter then displays the body of the
response (decoded in utf-8)
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL, an email and sends a POST request to the passed
    URL with the email as a parameter then displays the body of the
    response (decoded in utf-8)
    """
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html_str = html.decode('utf-8')
    print(html_str)
