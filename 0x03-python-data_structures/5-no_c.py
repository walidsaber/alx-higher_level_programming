#!/usr/bin/python3

def no_c(my_string):
    xlist = []
    x = 0
    while x < len(my_string):
        if my_string[x] != "C" and my_string[x] != "c":
            xlist += [my_string[x]]
        x += 1
    my_string = "".join(xlist)
    return my_string
