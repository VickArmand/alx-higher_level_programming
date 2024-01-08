#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            page = response.read()
        print(page.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
