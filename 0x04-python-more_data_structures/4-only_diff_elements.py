#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    xlist = []
    blist = []
    for x in set_1:
        if x in set_2:
            xlist += [x]
    for b in set_1:
        if b not in xlist:
            blist += [b]
    for b in set_2:
        if b not in xlist:
            blist += [b]
    return blist
