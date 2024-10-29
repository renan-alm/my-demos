#!/bin/bash

# Ensure curl and jq are installed
if ! command -v curl &> /dev/null; then
    echo "curl is not installed. Please install curl and try again."
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "jq is not installed. Please install jq and try again."
    exit 1
fi

# Call advice slip api
curl -s https://api.adviceslip.com/advice | jq -r '.slip.advice'

# Call a weather api for a specific location provided by the user
echo "Enter the location for which you want to get the weather information: "
read location
curl -s "https://wttr.in/$location?format=%C+%t" 
