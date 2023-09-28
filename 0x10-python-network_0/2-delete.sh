#!/bin/bash
# sends aand passes as the first argument a DELETE request to a given URL then displays the body of the response
curl -sX DELETE $1 -L
