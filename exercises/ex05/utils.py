"""EX05 - List Utility Functions cont. - Practice building lists and writing unit tests."""

__author__ = "730391892"


def only_evens(int_list: list[int]) -> list[int]:
    """Given a list of integers returns a list of only the even integers."""
    idx: int = 0
    list_evens: list = []
    while idx < len(int_list):
        if int_list[idx] % 2 == 0:
            list_evens.append(int_list[idx])
        idx += 1
    return list_evens


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given two lists concatenates the entries into one list."""
    list_concat: list = []
    idx: int = 0
    while idx < len(list_one):
        list_concat.append(list_one[idx])
        idx += 1
    idx = 0
    while idx < len(list_two):
        list_concat.append(list_two[idx])
        idx += 1
    return list_concat


def sub(input_list: list[int], idx_start: int, idx_end: int) -> list[int]:
    """Given a list of integers and indexes, returns a list of the entries between the indexes."""
    sub_list: list = []
    x: int = idx_start
    if idx_start < 0:
        x = 0
    elif idx_end > len(input_list):
        idx_end = len(input_list)
    elif len(input_list) == 0 or idx_start >= len(input_list) or idx_end <= 0:
        return sub_list
    while x < idx_end:
        sub_list.append(input_list[x])
        x += 1
    return sub_list