#!/usr/bin/python3
"""
displays the value of the variable X-Request-Id in the response header"""

import sys 
import requests

if __name__ == "__main__":
    re = requests.get(sys.argv[1])
    print(re.headers.get('X-Request-Id'))
