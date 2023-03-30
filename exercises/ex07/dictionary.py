"""EX07 - Dictionary Utilities - Practice with dictionary functions."""

__author__ = "730391892"


def invert(initialdict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, will invert the keys and the values."""
    key_list: list = []
    for key in initialdict:
        key_list.append(initialdict[key])
    entry_tally: dict = count(key_list)
    for key in entry_tally:
        if entry_tally[key] > 1:
            raise KeyError
    invertdict: dict[str, str] = {}
    for key in initialdict:
        invertdict[initialdict[key]] = key
    return invertdict


def favorite_color(colordict: dict[str, str]) -> str:
    """Returns the color, or key, that has the highest value."""
    color_count: dict[str, int] = {}
    color_list: list[str] = []
    fav_color: str = ""
    x: int = 0
    y: int = 1
    tally: int = 0
    for key in colordict:
        color_list.append(colordict[key])
    for x in range(0, len(color_list)):
        color_count[color_list[x]] = 1
        for y in range(x + 1, len(color_list)):
            if color_list[x] == color_list[y]:
                color_count[color_list[x]] += 1
            y += 1
        x += 1
    for key in color_count:
        if color_count[key] > tally:
            tally = color_count[key]
            fav_color = key
    return fav_color


def count(entries: list[str]) -> dict[str, int]:
    """Given a list will produce a dictionary with the entries as keys and the counts as values."""
    count_dict: dict[str, int] = {}
    x: int = 0
    for x in range(0, len(entries)):
        if entries[x] in count_dict:
            count_dict[entries[x]] += 1
        else:
            count_dict[entries[x]] = 1
        x += 1
    return count_dict