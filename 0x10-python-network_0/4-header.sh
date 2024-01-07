#!/bin/bash
# Bash script that takes in a URL, sends a GET request to it and displays the body of the response
# A header variable X-School-User-Id must be sent with the value 98
curl -sb X-School-User-Id=98 $1
