#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that makes the server to respond with a given message in response body
curl -o /dev/null -sw "You got me!" .0.0.0 :5000/catch_me
