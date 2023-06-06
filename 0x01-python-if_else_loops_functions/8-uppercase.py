#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (str[i] == '\n'):
            print("\n")
        print("{}".format(chr(ord(str[i])-32)), end='')

