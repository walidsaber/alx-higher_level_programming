#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        tuple_a = (0, 0)
    if not tuple_b:
        tuple_b = (0, 0)
    if len(tuple_a) != 2:
        x1 = tuple_a[0]
        x2 = 0
        tuple_a = x1, x2
    if len(tuple_b) != 2:
        x1 = tuple_b[0]
        x2 = 0
        tuple_b = x1, x2
    result = tuple(x + y for x, y in zip(tuple_a[:2], tuple_b[:2]))
    return result