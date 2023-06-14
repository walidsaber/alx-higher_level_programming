#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    x = 0
    for key in a_dictionary:
        if a_dictionary[key] > x:
            x = a_dictionary[key]
            max_score = key
    return max_score
