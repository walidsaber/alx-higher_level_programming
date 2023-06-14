#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    unique_nm = []
    for i in my_list:
        if i not in unique_nm:
            result += i
            unique_nm += [i]
    return result
