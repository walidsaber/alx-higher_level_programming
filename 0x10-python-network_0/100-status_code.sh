#!/bin/bash
# sc
curl -o /dev/null -sw "%{http_code}" $1
