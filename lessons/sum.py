"""Example function for unit tests"""

__author__ = "730391892"


def sum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    for idx in range(len(xs)):
        sum_total += xs[idx]
        idx += 1
    return sum_total