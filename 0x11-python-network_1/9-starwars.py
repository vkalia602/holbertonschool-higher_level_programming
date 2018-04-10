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
    url = "https://swapi.co/api/people/?search="
    url = url + q

    r = requests.get(url)
    data = r.json()
    try:
        print("Number of results: {}".format(data['count']))
    except ValueError:
        print("Not a valid JSON")

    names = data['results']
    for one in names:
        print(one['name'])
