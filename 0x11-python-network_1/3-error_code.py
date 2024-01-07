#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

import sys
from urllib import request, error, parse
respones = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    reqst = response.read().decode('utf8')
    print(reqst)
except urllib.error.HTTPError as err:
    print("Error code: {}".format(err.code))
