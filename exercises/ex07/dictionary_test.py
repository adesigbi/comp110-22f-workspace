"""Tests fucntions in dictionary."""

from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest


def test_invert() -> None:
    """Sees if the invert function is working."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert({'table': 'mouse'}) == {'mouse': 'table'}
    assert invert({'yellow': 'yellow', 'red': 'red'}) == {'yellow': 'yellow', 'red': 'red'}
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color() -> None:
    """Sees if the test_favorite_color function is working."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"
    assert favorite_color({"John": "green", "Hank": "green", "lauri": "pink", "tommy": "pink", "Mark": "pink"})
    assert favorite_color({"Hanna": "pink", "Joana": "yellow", "Cam": "green"}) == "pink"


def test_count() -> None:
    """Sees if the count function is working."""
    assert count(["s", "l", "s", "d", "n", "n", "n", "d"]) == {"s": 2, "l": 1, "d": 2, "n": 3}
    assert count(["s"]) == {"s": 1}
    assert count(["n", "n", "n", "n", "n", "n", "l", "n"]) == {"n": 7, "l": 1}