#!/usr/bin/env python3
"""Demonstrates mixins with SwimMixin, FlyMixin and Dragon."""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can swim, fly and roar."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
