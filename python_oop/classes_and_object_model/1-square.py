#!/usr/bin/env python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square's sides.
        """
        self.__size = size
