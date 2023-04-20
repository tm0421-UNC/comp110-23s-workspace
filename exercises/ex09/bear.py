"""File to define Bear class."""

__author__ = "730391892"


class Bear:
    """Bear in the river."""
    # Attributes
    age: int
    hunger_score: int
    
    def __init__(self):
        """Initializes bears."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Simulates one day for bears."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Adjusts hunger_score based on number of fish eaten."""
        self.hunger_score += num_fish
        return None
    
