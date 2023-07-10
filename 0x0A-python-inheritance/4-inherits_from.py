#!/usr/bin/python3
""" subclass formula """



def inherits_from(obj, a_class):
    """True or False"""
    return(issubclass(type(obj), a_class))
