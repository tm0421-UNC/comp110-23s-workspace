"""File to define River class."""

__author__ = "730391892"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River ecosystem in the simulation."""
    # Attributes
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):  
        """Checks that bears and fish are under specified ages."""
        new_bears: list = []
        new_fish: list = []
        for bear in self.bears:
            if bear.age > 5:
                None
            else:
                new_bears.append(bear)
        for fish in self.fish:
            if fish.age > 3:
                None
            else:
                new_fish.append(fish)
        self.bears = new_bears
        self.fish = new_fish
        return None
    
    def bears_eating(self):
        """Has each bear eat depending on the number of fish in the river."""
        for bear in self.bears:
            if len(self.fish) > 4:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks if any bears starved."""
        bears_survive: list = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bears_survive.append(bear)
        self.bears = bears_survive
        return None
    
    def repopulate_fish(self):
        """Repopulates the fish."""
        fish_offspring = (len(self.fish) // 2) * 4
        x: int = 0
        for x in range(0, fish_offspring):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulates the bears."""
        bear_offspring = len(self.bears) // 2
        x: int = 0
        for x in range(0, bear_offspring):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Displays statistics of the river."""
        x = self.day
        y = len(self.fish)
        z = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week."""
        while self.day < 7:
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes a specified number of fish from the river."""
        new_fish: list = []
        x: int = amount
        while x < len(self.fish):
            new_fish.append(self.fish[x])
       