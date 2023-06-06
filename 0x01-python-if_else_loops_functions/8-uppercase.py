#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{}\n".format(chr(ord(str[i])-32)), end='')
