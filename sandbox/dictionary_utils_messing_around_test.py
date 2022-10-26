"""Tests the dictionary_utils_messing_around module functions"""


import pytest
from dictionary_utils_messing_around import invert

def test_invert() -> None:
    """Sees if the invert function is working."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert({'table': 'mouse'}) == {'mouse': 'table'}
    assert invert({'yellow': 'yellow', 'red': 'red'}) == {'yellow': 'yellow', 'red': 'red'}
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)