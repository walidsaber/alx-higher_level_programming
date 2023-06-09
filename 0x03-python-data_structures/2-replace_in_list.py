#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if idx >= 0 and idx < x:
        my_list[idx] = element
    else:
        return None
    return my_list
