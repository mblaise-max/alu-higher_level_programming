#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


class Square:
    """Defines a square by its validated size."""

    def __init__(self, size=0):
        """Initializes a square, checking the type and value of size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
