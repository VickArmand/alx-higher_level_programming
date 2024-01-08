#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import requests


if __name__ == "__main__":
    values = {}
    values['email'] = sys.argv[2]
    req = requests.post(sys.argv[1], data=values)
    print(req.text)
