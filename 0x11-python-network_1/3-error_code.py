#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body
of the response
"""

if __name__ == "__main__":
    import urllib
    import sys
    import requests

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
