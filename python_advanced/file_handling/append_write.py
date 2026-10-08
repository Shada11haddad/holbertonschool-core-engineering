#!/usr/bin/env python3
"""
Module that defines append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF-8 text file, creating it if
    needed, and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
