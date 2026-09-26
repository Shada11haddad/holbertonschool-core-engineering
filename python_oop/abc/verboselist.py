#!/usr/bin/env python3
"""Defines VerboseList, a list that reports every change made to it."""


class VerboseList(list):
    """A list that prints a message when items are added or removed."""

    def append(self, item):
        """Add item to the end of the list and report it.

        Args:
            item: The item to add.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Add every item of iterable to the list and report how many.

        Args:
            iterable: The items to add.
        """
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Report and remove the first occurrence of item.

        Args:
            item: The item to remove.

        Raises:
            ValueError: If item is not in the list.
        """
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Report, remove and return the item at index (last by default).

        Args:
            index (int): The position of the item to pop.

        Returns:
            The popped item.

        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
