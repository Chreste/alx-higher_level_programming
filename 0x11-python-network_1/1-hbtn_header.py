#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen(url) as response:
        alx = response.read()
        print(alx['X-Request-Id'])

if __name__ == "__main__":
    url = sys.argv[1]
