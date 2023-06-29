#!/usr/bin/python3
"""lass Square."""


class Square:
    """square."""

    def __init__(self, size=0):
        """new square.
        Args:
            size (int):
        """
        self.size = size

    @property
    def size(self):
        """get/set size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the square."""
        return self.__size * self.__size
