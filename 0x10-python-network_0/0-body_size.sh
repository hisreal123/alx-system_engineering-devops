#!/usr/bin/env bash
# A Script that takes i a URL, sends a request to the URL, and displays the size of the body of the respon
curl -s "$1" | wc -c
