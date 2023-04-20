"""File to define Fish class."""

__author__ = "730391892"


class Fish:
    """Fish in the river."""
    # Atrributes
    age: int

    def __init__(self):
        """Initializes fish to be age 0."""
        self.age = 0
        return None
    
    def one_day(self):
        """Simulates one day for fish."""
        self.age += 1
        return None