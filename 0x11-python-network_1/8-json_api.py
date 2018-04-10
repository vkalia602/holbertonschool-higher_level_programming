#!/usr/bin/python3
"""
Script that takes a letter and sends a post request
"""

if __name__ == "__main__":
    import sys
    import requests

    try:
        q = sys.argv[1]
    except IndexError:
        q = ""

    r = requests.post("http://0.0.0.0:5000/search_user", {'q': q})
    data = {}
    data = r.json()
    try:
        if len(data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data.get('id'), data.get('name')))
    except:
        print("Not a valid JSON")
