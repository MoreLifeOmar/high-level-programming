#!/usr/bin/python3
"""Module Square"""


class Square:
    """Private Attribute"""
    def __init__(self, size=0):
        self.__size = size
        """Initialization"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    """Public instance"""
    def area(self):
        return self
