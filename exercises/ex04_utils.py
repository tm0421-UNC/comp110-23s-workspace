"""EX04 - List Utility Functions - An introductory exercise utilizing lists."""

__author__ = "730391892"


def all(int_list: list[int], int_given: int) -> bool:
    """Checks if all the integers in a list are equal to the given integer."""
    # Checks if the list is empty.
    if int_list == []:
        return False
    idx: int = 0
    all_same: int = 0 
    # Checks each index of the list for the given integer and counts the number of instances.
    while idx < len(int_list):
        if int_given == int_list[idx]:
            all_same += 1
        idx += 1
    # Looks if the number of instances equals the length of the list.
    if all_same == len(int_list):
        return True
    else:
        return False
    

def max(input: list[int]) -> int:
    """Returns the largest value given a list of integers."""
    # Checks if the list is empty.
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max_value: int = input[idx] 
    # Assigns first item in a list to max and checks each index of the list for a greater number.
    while idx < len(input):
        if max_value < input[idx]:
            max_value = input[idx]
        idx += 1
    return max_value

    
def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks each index of two lists and determines if they are equal."""
    idx: int = 0
    count: int = 0
    # Checks that the lists are the same length.
    if len(list_one) != len(list_two):
        return False
    else:
        # Checks each index of both lists for equal values.
        while idx < len(list_one):
            if list_one[idx] == list_two[idx]:
                count += 1
            idx += 1
        if count == len(list_one):
            return True
        else:
            return False
    
