#!/bin/bash
#Bash script that takes in a URL as an argument, sends a GET
curl -s "$1" GET -H "X-HolbertonSchool-User-Id: 98"
