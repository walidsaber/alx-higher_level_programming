#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            print("{}".format(chr(ord(str[i])-32)), end='')
        else:
            print("{}".format(str[i]))

