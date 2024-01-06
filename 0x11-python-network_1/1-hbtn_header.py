#!/usr/bin/python3
""" 
displays the value of the X-Request-Id variable found in the header of the response """

import urllib.request
from sys import argv
with urllib.request.urlopen(argv[1]) as response:
    alx = response.info()
    print(alx['X-Request-Id'])

if __name__ == "__main__":
