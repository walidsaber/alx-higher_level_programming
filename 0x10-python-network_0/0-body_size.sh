#!/bin/bash
# sc
curl -sI "$1" | grep -i Content-Length | cut -d " " -f
