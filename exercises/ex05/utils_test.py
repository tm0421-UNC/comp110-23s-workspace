"""EX05 - Utils Test - Unit Tests for List Utility Finctions."""

__author__ = "730391892"

from ex05_utils import only_evens, sub, concat


# Unit tests for only_evens function
def test_odds() -> None:
    """Tests that a list of odd numbers returns an empty list."""
    assert only_evens([1, 3, 5, 7]) == []


def test_mix() -> None:
    """Tests that a given a mix of integers will return a list of only even integers."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_empty() -> None:
    """Tests that given an empty list, returns an empty list."""
    assert only_evens([]) == []


# Unit tests for concat function
def test_() -> None:
    """Tests that given two lists, concatenates the entries."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_dif_len() -> None:
    """Tests that given two lists of different lengths, will concatenate the entries of integers."""
    assert concat([1], [4, 5, 6]) == [1, 4, 5, 6]


def test_one_list() -> None:
    """Tests that given two lists and one is empty, will return the non-empty list."""
    assert concat([1, 2, 3], []) == [1, 2, 3]


# Unit tests for sub function
def test_invalid_idx() -> None:
    """Tests that given invalid indexes, will return an empty list."""
    assert sub([1, 2, 3, 4], 3, 1) == []


def test_neg_start() -> None:
    """Tests that given a negative start index, will start at the beginning of the list."""
    assert sub([1, 2, 3, 4], -1, 4) == [1, 2, 3, 4]


def test_shorten() -> None:
    """Tests that given a list and two indexes, will return the entries between the indexes."""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]