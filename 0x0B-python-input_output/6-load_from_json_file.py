#!/usr/bin/python3
"""save to json file"""
import json


def load_from_json_file(filename):
    """object"""
    with open(filename, 'r') as f:
        return json.load(f)
