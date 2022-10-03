"""Tests cyoa functions"""

from exercises.cyoa import word_finder 

# def test_word_finder() -> None:
#     my_list: list[str] = ["a", "b", "c", "d", "e"]
#     assert word_finder("a", my_list) == "a"
#     assert word_finder("l", my_list) == "a"

my_list: list[str] = ["a", "b", "c", "d", "e"]
# word_finder("t", my_list)

from exercises import cyoa

def test_index_finder() -> None:
    assert cyoa.index_finder("c", my_list) == 2



