"""Reproducing abstractions with lists."""

__author__ = "730572167"


def all(xs: list[int], x: int) -> bool:
    """Finds if a list is made completly of a given integer."""
    assert len(xs) != 0
    i: int = 0
    while i < len(xs):
        if xs[i] != x:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Finds the largest interger in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    greatest_index: int = 0 
    lesser_index: int = 1 
    counter: int = 0
    while counter < (len(input) - 1):
        if input[greatest_index] < input[lesser_index]:
            greatest_index = lesser_index
        lesser_index += 1
        counter += 1
    return input[greatest_index]    


def is_equal(xs: list[int], ys: list[int]) -> bool:
    """Sees if two lists are identical."""
    i: int = 0 
    if len(xs) != len(ys):
        return False
    while i < len(xs):
        if xs[i] != ys[i]:
            return False
        i += 1
    return True