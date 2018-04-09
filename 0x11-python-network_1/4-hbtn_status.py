#!/usr/bin/python3
"""
Script that fetches "https://intranet.hbtn.io/status"
"""

if __name__ == "__main__":

    import sys
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    text = r.text
    r = str(r)
    print('Body response:')
    print('\t- type: {}'.format(type(r)))
    print('\t- content: {}'.format(text))
