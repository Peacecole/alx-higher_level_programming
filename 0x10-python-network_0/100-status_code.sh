#!/bin/bash
# sends a request to a given URL that is passed as an argument, and displays only the status code of the response.
curl -o /dev/null -sw "%{http_code}" $1
