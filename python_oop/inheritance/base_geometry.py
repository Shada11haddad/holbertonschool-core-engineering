#!/usr/bin/env python3
"""Defines the BaseGeometry class, the base for geometric shapes."""


class BaseGeometry:
    """Represents shared behavior for geometric shapes."""

    def area(self):
        """Compute the area of the shape.

        Raises:
            Exception: Always, since subclasses must implement it.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the value, used in error messages.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
