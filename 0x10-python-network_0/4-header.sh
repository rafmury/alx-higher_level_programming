#!/bin/bash

# Function to make a GET request
function make_get_request {
    local url="$1"
    local header="X-School-User-Id: 98"
    
    curl -s -H "$header" "$url"
}

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL from the command line argument
url="$1"

# Making the GET request and displaying the response body
echo "Hello School!"
make_get_request "$url"

