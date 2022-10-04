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
        userword = input("Sorry, that word was not one of the options. Recheck your spelling or see if item your referencing is still on your list and try again: ")
    return userword


def valid_word3(userword: str, option1: str, option2: str, option3: str) -> str:
    """Makes sure that an input by the user is a valid option given there are 3 options."""
    while (userword != option1) and (userword != option2) and (userword != option3):
        userword = input("Sorry, that word was not one of the options. Recheck your spelling or see if item your referencing is still on your list and try again: ")
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
    popped_item2_i = index_finder(popped_item2, item_list)
    item_list.pop(popped_item2_i)

    popped_item3: str = input("Pick the third object you want to throw overboard: ")
    popped_item3 = word_finder(popped_item3, item_list)
    popped_item3_i = index_finder(popped_item3, item_list)
    item_list.pop(popped_item3_i)

    popped_item4: str = input("Pick the fourth object you want to throw overboard: ")
    popped_item4 = word_finder(popped_item4, item_list)
    popped_item4_i = index_finder(popped_item4, item_list)
    item_list.pop(popped_item4_i)
    

def greet() -> None:
    """Greets the player and explains the situation."""
    global player
    #add emojis to welcome message
    player = input("Welcome to the game. What is your name?: ")
    input(f"Hi {player}, here is the current situation. prese enter to continue: ")


def stop_game() -> None:
    print(f"Goodbye {player}. In your experience, you gathered {points} adventure points. We hope you come to play again! ")
   

def boat1() -> None:
    """Actions happening given the user picks the first boat. Returns False when someone has died"""
    global points 
    global survivorship_score
    global items_score
    GAME_OVER: str = f"========Game Over=========\nIn your experience, you earned {points} points."
    item_list1: list[str] = ["first aid kit", "rope", "compass","army rations", "shaving mirror", "tent", "map of the atlantic", "plastic bags"]
    input("\nIn a rush, you board the first life raft. And by rummaging through the back of the raft, you find the following items\n ")
    for i in item_list1:
        print(i)
    input("**Keep in mind that the tent is perfectly made for the raft, and is not capable of being used for anything else \n")
    input("\nNow before you boarded the life raft, between gently sobbing and hopping into a boat, the last man working on the ship, gave a cryptic message explaining that \n"
    "the rafts are old so that if you were to keep all items on the ship, you would definitely drown. He said that you’d probably be safe if you only kept 5 of the items: \n")
    take_from_list(item_list1)
    points += 2
    input(f"Congrats {player}, you have completed your first task, and by doing so, you have earned 2 points. Your new point total is now {points}" )
    input("\n==========That Night==========\n")
    appropriate_materials1: bool = word_in_list("tent", item_list1)
    if appropriate_materials1 == False:
        input("It starts drizzling when you go to sleep. You hope that it doesn’t get worse because you don’t have the materials to protect yourself from the rain. \n")
        input(f"Uhoh {player}, the next morning you don't wake up, because in the middle of the night you died from hypothermia :(")
        print(GAME_OVER)
        return
    if appropriate_materials1 == True:
        rain_response: str = input("It starts to drizzle. Do you want to protect yourself from the rain or save energy and worry about that tomorrow? Type 'save energy' or 'protect from rain': ")
        rain_response = valid_word2(rain_response, "save energy", "protect from rain")
        if rain_response == "save energy":
            input("You soon hear thunderstorms. You try to sleep through the rain. \n")
            input(f"Uhoh {player}, it seems that the next morning, you die from hypothermia :(\n")
            print(GAME_OVER)
            return
        if rain_response == "protect from rain":
            input("You finish setting up the tent in just the nick of time. The storm reaches its head when you head inside.\n")
            input("You wake up tired but alive\n\n")
            points += 5
            input(f"Day 1 Completed: Congradulations {player}, you have earned 5 more points. Point total is now equal to {points}\n")
            input("\n =====The Next Day====\n")
            input("You start to get thirsty (who would have thought with your great lack of bottled water on hand). You know that it is due to rain in 2 more days. \n"
            "You also know that it takes a person roughly 3 days to die of starvation. Given this infromation, you decide you need to create a water collection system for rainfall.")
            if word_in_list("plastic bag", item_list1) == False:
                input("Unfortunatly, you very quickly realize that you do not have the materials to collect water.\n")
                input("The next day, out of desperation, you take in a mouthfull of the rubbing alcohol on the boat. You promptly vomit your insides out. And die within the hour.")
                print(GAME_OVER)
                return
            if word_in_list("plasitc bag", item_list1) == True:
                input("Here's a reminder of your list: ")
                for i in item_list1:
                    print(i)
                water_collector: str = input("\nWhat item from your list do you want to user to collect the water?: ")
                water_collector = word_finder(water_collector, item_list1)
                if water_collector != "plastic bag":
                    input(f"You try to muster together a water collection system with your {water_collector}. You then get inside of your tent and go off to sleep.\n")
                    input("In the morning, you see that your system has completely failed")
                    input("The next day, you die of dehydration.\n")
                    input("That is very sad for you :(")
                    print(GAME_OVER)
                    return
                if water_collector == "plastic bag":
                    points += 5
                    input("You set up your system with the plastic bag and it seems like it may work. You get inside your tent and then go off to sleep.\n")
                    input("In the morning, you see 5 bags full of water. After rejoicing you get back to business. ")
                    input(f"\nCongratulations {player}, you have successfully passed yet another day, you have 5 more points added. Your total is now {points}\n")

  
def main() -> None:
    greet()
    #present the user with three options 
    first_branch: str = input("\nThere are two empty life rafts available. You have no information about either rafts other than the fact that though both rafts\n"
    "should contain the materials for one to survive and be rescued within 10 days, the exact materials on the rafts vary slightly.\n \n"
    "Choose either boat 1 or boat 2 by typing “boat 1” or “boat 2”. If you do not want to continue playing the game, type “leave game”: ")
        
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
    print("End of loop")
    

if __name__ == "__main__":
    main()