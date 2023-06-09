#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return None
    hold_tuple = ()
    x = len(sentence)
    b = str(sentence[0])
    hold_tuple = x, b
    return hold_tuple
