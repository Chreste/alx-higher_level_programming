#!/bin/bash
# bash script for posting json data files and testing a server
curl -s -H "content-type:application/json"  -d @"$2" -X POST "$1"
