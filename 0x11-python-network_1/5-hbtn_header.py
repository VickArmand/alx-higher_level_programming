#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header
of the response.
You must use the packages requests and sys only
You must use get to access to dictionary value by key
(it won’t throw an exception if the key doesn’t exist in the dictionary)
"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
