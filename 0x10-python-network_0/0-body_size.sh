#!/bin/bash
# sc
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
