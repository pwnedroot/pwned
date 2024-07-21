#!/bin/bash

read -p "Enter a phone number to search for: " phoneNumber
phoneNumber="+1${phoneNumber}"

response=$(curl --silent --request GET "https://api.apilayer.com/number_verification/validate?number=$phoneNumber" --header "apikey: your_apilayer_api_right_here")

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Error: Curl request failed."
    exit 1
fi

# Check if response is empty
if [ -z "$response" ]; then
    echo "Error: Empty response from API."
    exit 1
fi

echo "$response"
