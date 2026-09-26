#!/usr/bin/env python3
"""Defines a Square class that can compute its area and print itself."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.size = size

    @property
    def size(self):
        """int: The size of the square's sides."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating it.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character, or an empty line if 0."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
