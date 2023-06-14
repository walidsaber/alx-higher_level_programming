#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    xlist = []
    for x in a_dictionary:
        if a_dictionary[x] == value:
            xlist += [x]
    for i in xlist:
        del a_dictionary[i]
    return a_dictionary
