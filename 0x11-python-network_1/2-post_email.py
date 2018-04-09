#!/usr/bin/python3
"""
Script takes a URL and sends a post request with email parameter
"""

if __name__ == "__main__":
    from urllib.request import urlopen
    import urllib
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urlopen(req) as response:
        page = response.read()
        print(page.decode('utf-8'))
