#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request  to the passed URL"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data, method="POST")
    with request.urlopen(req) as respone:
        print(response.read().decode('utf-8'))
