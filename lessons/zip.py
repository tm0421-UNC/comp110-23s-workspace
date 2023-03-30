"""CQ04 - Dict Function Writing"""

__author__ = "730391892"

def zip(keys: list[str], items: list[int]) -> dict[str, int]:
    dictionary: dict[str, int] = {}
    empty: dict = {}
    x: int = 0
    if len(keys) != len(items) or keys == [] or items == []:
        return empty
    else: 
        while x < len(items):
            dictionary[keys[x]] = items[x]
            x += 1
        return dictionary

