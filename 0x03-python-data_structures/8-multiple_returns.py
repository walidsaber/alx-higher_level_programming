#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
        return sentence
    hold_tuple = ()
    x = len(sentence)
    b = str(sentence[0])
    hold_tuple = x, b
    return hold_tuple
