#!/bin/bash
# takes in and sends a request to a given URL, and displays the size of the body of the response
curl -sX GET $1 -L
