#!/bin/bash
# Script that makes a request to causes an specific response
curl -sLX PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
