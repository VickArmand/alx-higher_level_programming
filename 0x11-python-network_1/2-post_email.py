#!/usr/bin/python3
""""""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    values = {}
    values['email'] = sys.argv[2]
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()
    print(resp.decode('utf-8'))
