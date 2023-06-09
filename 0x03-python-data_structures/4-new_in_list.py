#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    xlist = my_list.copy()
    x = len(my_list)
    if idx >= 0 and idx < x:
        xlist[idx] = element
    else:
        return my_list
    return xlist
