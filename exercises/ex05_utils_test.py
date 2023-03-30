"""EX05 - Utils Test - Unit Tests for List Utility Finctions"""

__author__ = "730391892"

from ex05_utils import only_evens, sub, concat

#Unit tests for only_evens function
def test_odds() -> None:
    """Tests that a list of odd numbers returns an empty list."""
    assert only_evens([1, 3, 5, 7]) == []

def test_mix() -> None:
    """Tests that a given a mix of integers will return a list of only even integers."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]

def test_empty() -> None:
    assert only_evens([]) == []

#Unit tests for concat function
def test_() -> None:
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3]

def test_dif_len() -> None:
    assert concat([1], [4, 5, 6]) == [1, 4, 5, 6]

def test_empty() -> None:
    assert concat([1, 2, 3], []) == [1, 2, 3]

#Unit tests for sub function
def test_incorrect_idx() -> None:
    assert sub([1, 2, 3, 4], 3, 1) == []

def test_neg_start() -> None:
    assert sub([1, 2, 3, 4], -1, 4) == [1, 2, 3, 4]

def test_shorten() -> None:
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
