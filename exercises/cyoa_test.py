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

def boat2(points: int) -> None:
    """Actions that happen after the user picks the second boat."""
    item_list2: list[str] = ["pocket knife", "map of the atlantic", "compass", "fishing kit", "a bucket", "tarp and sleeping bag", "rubbing alcohol", "petroleum/oil mixture"]
    input("\nWithout much thinking, you chose the second life raft. And by rummaging through the back of the raft, you find the following items\n")
    for i in item_list2:
        print(i)
    input("**Keep in mind that petroleum/oil mixture also comes with matches. It is also not capable of being used for cooking or powering the raft. \n")
    input("\nNow before you boarded the life raft, between gently sobbing and hopping into a boat, the last man working on the ship, gave a cryptic message explaining that \n"
    "the rafts are old so that if you were to keep all items on the ship, you would definitely drown. He said that you’d probably be safe if you only kept 4 of the items: \n")
    cyoa.take_from_list(item_list2)
    points += 2
    input(f"Congrats {cyoa.player}, you have completed your first task, and by doing so, you have earned 2 points. Your new point total is now {points}: " )
    shark_survival_chance: int(1, 100)
    previous_score: int = points
    print(item_list2)
    for i in item_list2:
        if (i == "fishing kit") or (i == "a bucket") or (i == "tarp and sleeping bag") or (i == "petroleum/oil mixture"):
            points += 5
    print(f"Points: {points}")
    print(f"Previous points: {previous_score}")

boat2(0)
