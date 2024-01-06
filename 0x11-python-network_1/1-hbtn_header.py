#!/usr/bin/python3
""" 
displays the value of the X-Request-Id variable found in the header of the response """

import urllib.request
from sys import argv

def main(argv):
    with urllib.request.urlopen(argv[1]) as response:
        alx = response.info()
        if 'X-Request-Id' in alx:
            print(alx['X-Request-Id'])
        else:
            print("X-Request-Id header isn't present in the response")

if __name__ == "__main__":
    if len(argv) < 2:
        print("you need to provide a url.")
        sys.ext(1)
    main(argv)
