#!/usr/bin/env bash
# Bash script that takes in a URL as first parameter, sends a DELETE request to it and displays body of response
curl -X DELETE $1
