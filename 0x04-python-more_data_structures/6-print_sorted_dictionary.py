#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    xlist = sorted(a_dictionary)
    for i in xlist:
        print("{}: {}".format(i, a_dictionary[i]))
