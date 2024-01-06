#!/usr/bin/python3
""" 
displays the value of the X-Request-Id variable found in the header of the response """

import sys
import urllib.request

if __name__ == " __main__":
    with urllib.request.urlopen(argv[1]) as response:
        alx = response.info()
        print(alx['X-Request-Id'])
