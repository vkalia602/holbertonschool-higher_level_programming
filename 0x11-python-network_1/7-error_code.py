#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body
of the response
"""

if __name__ == "__main__":
    import sys
    import requests

    r = requests.get(sys.argv[1])
    if r.status_code <= 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
