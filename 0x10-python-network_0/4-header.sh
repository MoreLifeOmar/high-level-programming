#!/bin/bash
#Bash script that takes in a URL as an argument, sends a GET
curl -s "$1" GET -H "X-School-User-Id: 98"
