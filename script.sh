#!/bin/bash

# Ensure curl is installed
if ! command -v curl &> /dev/null
then
    echo "curl could not be found, installing..."
    sudo apt-get update
    sudo apt-get install -y curl
fi

# ensure jq is installed
if ! command -v jq &> /dev/null
then
    echo "jq could not be found, installing..."
    sudo apt-get install -y jq
fi

# Call the Advice Slip API and display a random advice
response=$(curl -s https://api.adviceslip.com/advice)
advice=$(echo $response | jq -r '.slip.advice')
echo "Here is a piece of advice: $advice"