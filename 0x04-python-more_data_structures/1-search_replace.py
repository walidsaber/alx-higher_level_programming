#!/usr/bin/python3

def search_replace(my_list, search, replace):
    cnt = 0
    xlist = []
    for i in my_list:
        if i == search:
            xlist += [replace]
        else:
            xlist += [my_list[cnt]]
        cnt += 1
    return xlist
