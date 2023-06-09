#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    xtuple = tuple(map(sum, zip(tuple_a, tuple_b)))
    return xtuple
