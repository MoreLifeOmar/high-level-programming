#!/usr/bin/python3
"""write file."""


def write_file(filename="", text=""):
    """write file."""
    with open(filename, mode='w', encoding='UTF8') as f:
        chars = f.write(text)
    return chars
