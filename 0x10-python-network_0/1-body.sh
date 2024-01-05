#!/bin/bash
# Take in URL, display body of a 200 response
curl -sfL "$1" -X GET
