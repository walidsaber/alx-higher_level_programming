#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    b_dic = {}
    for ky,val in a_dictionary.items():
        b_dic[ky] = val*2
    return b_dic
