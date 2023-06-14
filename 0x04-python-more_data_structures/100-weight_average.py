#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0.0
    b = 0.0
    for i, y in my_list:
        a += (i * y)
        b += y
    return float(a/b)
