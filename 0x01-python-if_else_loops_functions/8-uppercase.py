#!/usr/bin/python3
def uppercase(str):
    stored = ""
    for i in range(len(str)):
        if (ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            stored = stored + chr(ord(str[i])-32)
        else:
            stored = stored + str[i]
    print("{}".format(stored), end='\n')
