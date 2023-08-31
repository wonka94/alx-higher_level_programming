#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file and displays the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
