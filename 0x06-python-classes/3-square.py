#!/usr/bin/python3
# 3-square.py
"""class Square."""


class Square:
    """square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int):
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of the square."""
        return self.__size * self.__size
