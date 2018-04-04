#!/bin/bash
#sends a POST request to the passed URL, and displays response
curl -s -X POST -d  "subject: I will always be here for PLD&email: hr@holbertonschool.com" "$1"
