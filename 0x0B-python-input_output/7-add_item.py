#!/usr/bin/python3
"""Adds all arguments to a Python list."""
from sys import argv
from os import stat, path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """main module"""
    file = "add_item.json"
    if path.isfile(file) and stat(file).st_size != 0:
        av = load_from_json_file(file)
    else:
        av = []
    av.extend(argv[1:])
    save_to_json_file(av, file)


if __name__ == "__main__":
    main()
