#!/usr/bin/python3

import sys

def args_counts():
    args = sys.argv[1:]
    argc = len(args)
    if argc > 0:
        dot = ":"
    else:
        dot = ""
    print(f"{argc} arguments{dot}")
    for i in range(len(args)):
        print(f"{i+1}: {args[i]}")

args_counts()
