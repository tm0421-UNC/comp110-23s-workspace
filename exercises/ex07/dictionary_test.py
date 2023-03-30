"""EX07 - Dictionary Utilities - Unit tests for dictionary functions."""

__author__ = "730391892"

from ex07 import invert, favorite_color, count


def test_empty() -> None:
    """Tests that an empty dictionary returns an empty dictionary."""
    assert invert({}) == {}


def test_normal() -> None:
    """Tests that a dictionary will return a dictionary with keys and values switched."""
    assert invert({'a': 'z', 'b': 'y'}) == {'z': 'a', 'y': 'b'}
    

def test_int() -> None:
    """Tests that a dictionary with integers will be properly inverted."""
    assert invert({1: 'j', 2: 'l'}) == {'j': 1, 'l': 2}


def test_fav() -> None:
    """Tests that given a dictionary of favorite colors, will return the color that appears most frequently."""
    assert favorite_color({'Mike': 'green', 'Joe': 'blue', 'Bob': 'blue'}) == 'blue'


def test_multfav() -> None:
    """Tests that when there are two modes for favorite color, will return the color that appeared first in the dictionary."""
    assert favorite_color({'Mike': 'green', 'Joe': 'blue'}) == 'green'


def test_integer() -> None:
    """Tests that given a dictionary with incorrect parameters will result in an error."""
    assert favorite_color({'Mike': 1, 'Joe': 2}) == 2


def test_oneval() -> None:
    """Tests that given a list with one item will return a dictionary with the item and a count of 1."""
    assert count(['green']) == {'green': 1}


def test_multval() -> None:
    """Tests that given a list with multiple items will return a dictionary with the item counts."""
    assert count(['green', 'blue', 'green']) == {'green': 2, 'blue': 1}


def test_emptylist() -> None:
    """Tests that given an empty list will return an empty dictionary."""
    assert count([]) == {}