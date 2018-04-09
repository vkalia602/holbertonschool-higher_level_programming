#!/usr/bin/python3
"""
This Script takes in a URL, sends a request to the URL and displays the
value of the x-request-ID variable in the header response
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
