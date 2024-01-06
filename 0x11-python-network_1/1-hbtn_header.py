#!/usr/bin/python3

import sys

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as response:
        alx = response.info()
        print(alx['X-Request-Id'])
