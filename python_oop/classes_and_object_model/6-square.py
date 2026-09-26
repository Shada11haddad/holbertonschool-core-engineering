#!/usr/bin/env python3
"""Defines a Square class with a size, a position and a printable form."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
            position (tuple): The (x, y) offset used when printing.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: The (x, y) offset of the square when printed."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validating it.

        Args:
            value (tuple): The new position, 2 integers >= 0.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character, shifted by position."""
        print(self)

    def __str__(self):
        """Return the square drawn with #, or an empty string if size is 0."""
        if self.__size == 0:
            return ""
        row = " " * self.__position[0] + "#" * self.__size
        lines = [""] * self.__position[1] + [row] * self.__size
        return "\n".join(lines)
