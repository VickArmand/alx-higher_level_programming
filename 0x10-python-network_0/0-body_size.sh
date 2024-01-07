#!/bin/bash
# Bash script that takes in a URL, sends a request to it and displays the size of body of response
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
