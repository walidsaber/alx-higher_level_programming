#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    x = 0
    maxx = 0
    while x < len(my_list):
        if my_list[x] > maxx:
            maxx = my_list[x]
        x += 1
    return int(maxx)
