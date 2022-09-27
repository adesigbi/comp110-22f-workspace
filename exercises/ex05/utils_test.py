"""Tests util functions"""

__author__ = "730572167"

from utils import only_evens
from utils import concat
from utils import sub


def test_only_evens() -> None:
    assert only_evens([]) == [] 
    assert only_evens([1, 8, 3, 4]) == [8, 4]
    assert only_evens([1, 5, 3]) == []



def test_concat() -> None:
    assert concat([], [1, 3, 4]) == [1, 3, 4]
    assert concat([], []) == []
    assert concat([1, 3, 4], []) == [1, 3, 4]
    assert concat([1], [2])  == [1, 2]
    assert concat([1, 3, 8], [2, 4, 4]) == [1, 3, 8, 2, 4, 4]


def test_sub() -> None:
    assert sub([10, 20, 30, 80], 1, 3) == [20, 30]
    assert sub([4, 7, 0], 1, 3) == [7, 0]
    assert sub([], 2, 3) == []
    assert sub([10, 20, 30, 80], 4, 1) == []
    assert sub([10, 20, 30, 80], 0, 0) == []
    assert sub([10, 20, 30, 80], -33, 9) == [10, 20, 30, 80]

