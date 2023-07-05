#!/usr/bin/python3
""" mod """


def text_indentation(text):
    """ print txt modif"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for xx in ".:?":
        text = (xx + "\n\n").join(
                [line.strip(" ") for line in text.split(xx)])

        print("{}".format(text), end="")
