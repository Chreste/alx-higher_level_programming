#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

import sys
from urllib import request, error, parse

def send_post_request(url, email):
    data = urllib.parse.urlencode({"email": email}).encode('utf-8')
    req = urllib.request.Request(url, data, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
