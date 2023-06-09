#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    xlist = []
    x = 0
    for i in my_list:
        if i % 2 == 0:
            xlist += [True]
        else:
            xlist += [False]
        x += 1
    return xlist
