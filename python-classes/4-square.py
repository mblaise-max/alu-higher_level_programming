#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """Defines a square with a validated size property."""

    def __init__(self, size=0):
        """Initializes a square using the size setter for validation."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square after validating it."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
