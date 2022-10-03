"""A ship wreck choose your own adventure game."""


__author__ = "730572167"

from random import randint
points: int = 0 
survivorship_score: int = 0
items_score: int = 0 
player: str = ""

def valid_word2(userword: str, option1: str, option2: str) -> str:
    """Makes sure that an input by the user is a valid option given there are 2 options."""
    while (userword != option1) and (userword != option2):
        userword = input("Sorry, that word was not one of the options. Recheck your spelling and try again: ")
    return userword

def valid_word3(userword: str, option1: str, option2: str, option3: str) -> str:
    """Makes sure that an input by the user is a valid option given there are 3 options."""
    while (userword != option1) and (userword != option2) and (userword != option3):
        userword = input("Sorry, that word was not one of the options. Recheck your spelling and try again: ")
    return userword


def word_in_list(word: str, list: list[str]) -> bool: 
    for item in list:
        if item == word:
            return True
    return False

def word_finder(word: str, list: list[str]) -> str:
    """Sees if a given word is a part of a given list and returns that word if it is""" 
    while word_in_list(word, list) == False:
        word = input("Sorry, the item you typed is not in the list. Recheck your spelling and try again: ")
    return word
        


def index_finder(word: str, list: list[str]) -> int:
    """Finds the index of a given word in a list"""
    i: int = 0 
    while i < len(list):
        if word == list[i]:
            return i
        i += 1

def take_from_list(item_list: list[str]) -> None:
    """Prompts the player to take 4 items from a list"""
    popped_item1: str = input("Pick the first of four objects you want to get rid of: ")
    popped_item1 = word_finder(popped_item1, item_list)
    popped_item1_i = index_finder(popped_item1, item_list)
    item_list.pop(popped_item1_i)

    popped_item2: str = input("Pick the second object you want to throw overboard: ")
    popped_item2 = word_finder(popped_item2, item_list)
    poped_item2_i = index_finder(popped_item2, item_list)

    popped_item3: str = input("Pick the third object you want to throw overboard: ")
    popped_item3 = word_finder(popped_item3, item_list)
    poped_item3_i = index_finder(popped_item3, item_list)

    popped_item4: str = input("Pick the fourth object you want to throw overboard: ")
    popped_item4 = word_finder(popped_item4, item_list)
    poped_item4_i = index_finder(popped_item4, item_list)
    print(item_list)



def greet() -> None:
    """Greets the player and explains the situation."""
    global player
    player = input("Welcome to the game. What is your name?: ")
    input(f"Hi {player}, here is the current situation. prese enter to continue: ")


def stop_game() -> None:
    print(f"Goodbye {player}. In your experience, you gathered {points} adventure points. We hope you come to play again! ")
   

def boat1() -> None:
    """Actions happening given the user picks the first boat."""
    global points 
    global survivorship_score
    global items_score
    item_list1: list[str] = ["first aid kit", "2 watter bottles", "sponges", "compass", "army rations", "shaving mirror", "tent", "map of the atlantic", "plastic bags"]
    input("\nIn a rush, you board the first life raft. And by rummaging through the back of the raft, you find the following items (press enter to continue the future dialogue): \n ")
    input(f"\n{item_list1}\n")
    input("\nNow before you boarded the life raft, the last man working on the ship, between gently sobbing and hopping into a boat, gave a cryptic message explaining that \n"
    "the rafts are old so that if you were to keep all items on the ship, you would definitely drown. He said that you’d probably be safe if you only kept 5 of the items.\n")
    take_from_list(item_list1)
    input(f"Here is the your new list of items\n{item_list1}")
    

    
    


def main() -> None:
    greet()
    #present the user with three options 
    first_branch: str = input("\nThere are two empty life rafts available. You have no information about either rafts other than the fact that though both rafts\n"
    "should contain the materials for one to survive and be rescued within 10 days, the exact materials on the rafts vary slightly.\n \n"
    "Choose either boat 1 or boat 2 by typing “boat 1” or “boat 2”. If you do not want to continue playing the game, type “leave game”: \n")
        
    first_branch = valid_word3(first_branch, "boat 1", "boat 2", "leave game")
    if first_branch == "boat 1":
        #run boat1 (interacts directly with global point values)
        boat1()
    elif first_branch == "boat 2":
        #run day one dumb decision
        print("second branch breached") #argument includes the current points your working with: 0, when dies, include an emoji appriate for the death(starvation, hypothermia, dehydration, drowning, shark attack)
    elif first_branch == "leave game":
        #stop the program, summed adventure points
        stop_game()
    
    
    
    


if __name__ == "__main__":
    main()