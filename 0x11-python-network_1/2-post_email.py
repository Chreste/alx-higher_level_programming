#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request  to the passed URL"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    try:
        data = parse.urlencode({"email": argv[2]}).encode('utf-8')
        req = request.Request(argv[1], data, method="POST")
        with request.urlopen(req) as respone:
            print(response.read().decode('utf-8'))
    except IndexError:
        print("Usage")
