#!/bin/bash
# script that takes in a URL, sends request to it and displays the
# size of the body of response

curl -s "$1" | grep "Content-Length:" | cut -d " " -f2
