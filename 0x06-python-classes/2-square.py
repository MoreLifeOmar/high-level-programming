#!/usr/bin/python3
"""Module Square"""


class Square:
    """Private Attribute"""
    def __init__(self, size=0):
        """Initialization"""
        self.__size = size
        """TypeError Exception"""
        try:
            size(int(input))
        except TypeError:
            raise Exception("size must be an integer")
        """ValueError Exception"""
        try:
            size >= 0
        except ValueError:
            raise Exception("size must be >= 0")
