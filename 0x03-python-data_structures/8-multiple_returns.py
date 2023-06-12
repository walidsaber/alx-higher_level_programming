#!/usr/bin/python3

def multiple_returns(sentence):
    hold_tuple = ()
    if not sentence:
        hold_tuple = 0, "None"
        return hold_tuple
    x = len(sentence)
    b = str(sentence[0])
    hold_tuple = x, b
    return hold_tuple
