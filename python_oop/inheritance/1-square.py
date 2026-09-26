#!/usr/bin/env python3
"""Defines a Square class, a subclass of Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a rectangle with equal width and height."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
