#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

import sys
from urllib import request, error
if __name__ == "__main__":
    try:
        resp = request.Request(sys.argv[1])
        with request.urlopen(resp) as response:
            reqst = response.read().decode('utf8')
            print(reqst)
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
