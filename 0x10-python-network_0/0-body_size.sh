#!/bin/bash
# script that takes in a URL, sends request to it and displays the size
curl -Is "$1" | grep "Content-Length:" | cut -d " " -f2
