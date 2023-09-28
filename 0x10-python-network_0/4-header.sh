#!/bin/bash
# takes in as an argument aand sends a GET request to a given URL then displays the body of the response
curl -sX GET $1 -H "X-School-User-Id: 98" -L
