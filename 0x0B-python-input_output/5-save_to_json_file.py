#!/usr/bin/python3
"""save to json mod"""
import json


def save_to_json_file(my_obj, filename):
    """w"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
