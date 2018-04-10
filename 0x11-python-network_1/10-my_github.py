#!/usr/bin/python3
"""
script that takes your Github credentials (username and password) and uses
the Github API to display your id
"""
if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    un = sys.argv[1]
    pswd = sys.argv[2]

    r = requests.get("https://api.github.com/user".format(un),
                     auth=HTTPBasicAuth(un, pswd))
    data = r.json()

    print(data.get('id'))
