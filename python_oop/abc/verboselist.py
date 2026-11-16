#!/usr/bin/env python3
"""Defines VerboseList, a list that announces its changes."""


class VerboseList(list):
    """List that prints a message when items are added or removed."""

    def append(self, item):
        """Add item to the end of the list and announce it."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Add all items to the list and announce how many were added."""
        size_before = len(self)
        super().extend(items)
        print("Extended the list with [{}] items.".format(
            len(self) - size_before))

    def remove(self, item):
        """Announce and remove the first occurrence of item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Announce, remove and return the item at index."""
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
