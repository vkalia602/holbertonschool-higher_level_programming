#!/bin/bash
#sends a POST request to the passed URL, and displays response
curl -sX POST -d  "subject=I will always be here for PLD&email=hr@holbertonschool.com" "$1"
