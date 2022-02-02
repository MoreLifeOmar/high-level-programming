#!/usr/bin/python3
"""
adds argv to a Python list, and save them to a file
"""
import sys

_save = __import__('5-save_to_json_file').save_to_json_file
_load = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    x = _load("add_item.json")
except ValueError:
    x = []
_save(x + sys.argv[1:], "add_item.json")
