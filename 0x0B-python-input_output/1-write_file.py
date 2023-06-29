#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
        writes a string to a text file (UTF8)
        returns the number of characters written
    """
    with open(filename, "w") as f:
        return f.write(str(text))
