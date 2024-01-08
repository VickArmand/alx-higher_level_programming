#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    page = response.read()
print("Body response:")
print("    - type: {}".format(type(page)))
print("    - content: {}".format(page))
print("    - utf8 content: {}".format(page.decode("utf-8")))
