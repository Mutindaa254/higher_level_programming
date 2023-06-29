#!/usr/bin/python3
"""script that takes in a URL and displays the body of the response 
(decoded in utf-8)
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    request = requests.post(url, data=values)
    print(request.text)
