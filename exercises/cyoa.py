"""A ship wreck choose your own adventure game."""


__author__ = "730572167"

from random import randint
points: int = 0 
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
    input(f"Hi {player}, here is the current situation. prese enter to continue through the rest of these prompts: ")


def stop_game() -> None:
    print(f"Goodbye {player}. In your experience, you gathered {points} adventure points. We hope you come to play again! ")
   

def boat1() -> None:
    """Actions happening given the user picks the first boat."""
    global points 
    item_list1: list[str] = ["first aid kit", "battery powered radio", "compass","army rations", "shaving mirror", "tent", "matches", "plastic bags"]
    input("\nIn a rush, you board the first life raft. And by rummaging through the back of the raft, you find the following items\n")
    for i in item_list1:
        print(i)
    input("**Keep in mind that the tent is perfectly made for the raft, and is not capable of being used for anything else \n")
    input("\nNow before you boarded the life raft, between gently sobbing and hopping into a boat, the last man working on the ship, gave a cryptic message explaining that \n"
    "the rafts are old so that if you were to keep all items on the ship, you would definitely drown. He said that you’d probably be safe if you only kept 5 of the items: \n")
    take_from_list(item_list1)
    points += 2
    input(f"Congrats {player}, you have completed your first task, and by doing so, you have earned 2 points. Your new point total is now {points}: " )
    input("\n==========That Night==========\n")
    appropriate_materials1: bool = word_in_list("tent", item_list1)
    if appropriate_materials1 == False:
        input("It starts drizzling when you go to sleep. You hope that it doesn’t get worse because you don’t have the materials to protect yourself from the rain. \n")
        input(f"Uhoh {player}, the next morning you don't wake up, because in the middle of the night you died from hypothermia :(")
        print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
        return
    if appropriate_materials1 == True:
        rain_response: str = input("It starts to drizzle outside. You realize that you have the materials to protect youself if the rain gets worse but, you don't really have the energy to.\n"
        "Do you want to protect yourself from the rain or save energy and worry about shelter tomorrow? Type 'save energy' or 'protect from rain': ")
        rain_response = valid_word2(rain_response, "save energy", "protect from rain")
        if rain_response == "save energy":
            input("You soon hear thunderstorms. You try to sleep through the rain. \n")
            input("Uhoh, you've died of hypothermia :(\n")
            print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
            return
        if rain_response == "protect from rain":
            input("You use your tent to build shelter and do so just in the nick of time. The storm reaches its head when you head inside.\nYou would have surely died of hypothermia if you had decided to sleep exposed to the elements. ")
            input("You wake up tired but alive. ")
            points += 5
            input(f"\nDay 1 Completed: Congradulations {player}, you have earned 5 more points. Point total is now equal to {points}\n")
            input("\n =====The Next Day====\n")
            input("You start to get thirsty and happen to have expert meteorological skills that allow you to be sure that the next rainfall is due for tonight,\n"
                "and that the next rainfall after that is due in 7 days. You also know that it takes a person roughly 3 days to die of dehydration.\nGiven this infromation, you understand that now is your ownly chance to make an effective water collection system.")
            input("Here's a reminder of your list:\n")
            for i in item_list1:
                print(i)
            water_collector: str = input("\nWhat item from your list do you want to user to collect the water tonight?: ")
            water_collector = word_finder(water_collector, item_list1)
            if water_collector != "plastic bags":
                input(f"You try to muster together a water collection system with your {water_collector}. You then get inside of your tent and go off to sleep.\n")
                input("In the morning, you see that your system has completely failed")
                input("\n=====Day 2=====\n")
                input("The thirst and dissapointment from your past actions starts settling in.")
                input("\n=====Day 3=====\n")
                input("You understand your fate and in vain, take in mouthfulls of ocean water, hoping that what all those 'scientist' say about osmosis and salt was wrong. \nYou promptly vomit and within the hour, start to hallucinate.")
                input("\n====Day 4=====\n")
                input("You die of dehydration. That is very sad for you :(")
                print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
                return
            if water_collector == "plastic bags":
                points += 5
                input("You set up your system with the plastic bags and it seems like it may work. You get inside your tent and then go off to sleep.\n")
                input("In the morning, you see 5 bags full of water. After rejoicing you get back to business. ")
                input(f"\nCongratulations {player}, you have successfully passed yet another day. You have 5 more points. Your total is now {points}\n")
                input("\n======Day 4=======\n")
                if word_in_list("army rations", item_list1) == False:
                    input("Oh no, it looks like there is no food in the items that you originally chose. \n")
                    input("\n=====Day 5=====\n")
                    input("You have gone 5 days without food and you think that the hunger is subsiding. \n"
                    "You continue your daily rituals and make sure your water collection system is still working well.")
                    input("\n=====Day 6=====\n")
                    input("You are craving something to eat again. Delirious and disappointed in your past decisions, you try catching fish. \n"
                    "In an attempt to grab a salmon with your bare hands, you fall overboard.")
                    input("Sorry, you died from drowning")
                    print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
                    return 
                if word_in_list("army rations", item_list1) == True: 
                    input("You start tearing into your army rations and begin to create rituals to mantian your suvrival.\n"
                    "You wake in the morning, pack up your tent to conserve space, have the breakfast of chapions that is canned meats and stale bread,\n"
                    "tinker with your objects on your person to try to make tools, eat dinner a of canned beans and crackers, set up up your tent again,\n"
                    "sleep, and do the same thing over again. You have all your basic necessities covered.")
                    input("\n=====Day 5=====\n")
                    input("Life isn't amazing, but it's managable. Maybe you could be a seaman forever you think. ")
                    input("\n=====Day 9=====\n")
                    input("On the horizon you see a passing ship. You realize that this may be one of your only opportunities to get back home. ")
                    input("You yell for a bit trying to get the ship's attention, and then realize that the ship is far too distanct for the people on it to hear you.\nYou need to use one of the items on you to signal them.")
                    input("Here’s a reminder of the your list:\n")
                    for i in item_list1:
                        print(i)
                    saving_item: str = input("\nWhich item do you choose to use?: ")
                    saving_item = word_finder(saving_item, item_list1)
                    if saving_item != "shaving mirror":
                        input(f"You try all the moves in the playbook to make your {saving_item} get the ships attention. But nothing works. The ship slips out from view on the horizon. ")
                        input("\n====Some time in the future====\n")
                        ending: int = randint(1, 4)
                        if ending == 1:
                            input("You have become accustomed with your life at sea, and you live your best seafaring life. You figured out how to catch fish and turtles for food. \n"
                            "You even have some heads from the turtle shells.")
                            input("You die at the age of 60, having never seen a human being again. ")
                            input("Did you win? Most wouldn't say so. But in your heart, on your death raft aged and wise, you thought 'surely I did.'")
                            input("You were never saved")
                        if ending == 2:
                            input("On day 14, you fought a losing battle with a hord of sharks. In the throws of action with the sea creatures, you thought that it was probably niave to think\n"
                            "that you'd survive months on the atlantic scratch free. That would require some great stroke of luck. Another boat came back around on the 24th day.")
                            input("You were never saved")
                        if ending == 3:
                            input("On the 24th day, another boat would come by, this time within yellig distance of your raft. Unfortunately, on your 23rd day you slept and walked off of the raft.\n")
                            input("You were never saved")
                        if ending == 4:
                            input("On day 103, you caught sight of an island. You mustered all your strength to make it to shore. And after stumbling around the sandy beach and \n"
                            "rejoicing for your first sighting of trees and stable ground in months, you were promptly killed by an archer from the island who mistook you for an animal.\n")
                            input("You were never saved")
                    if saving_item == "shaving mirror":
                        points += 5
                        input("You use the mirror to try to reflect the sun in the direction of the boat and by some miracle the small ship on the horizon becomes bigger and bigger,\n"
                        "until it is close enough for you to board it.")
                        input("You are saved")
                        input("You will tell your accolades to family and strangers alike and sue the cruise line involved in the sinking of your vessel, gaining a fortune in the process.")
                        input("Though a pretty unfortunate event happened to you, you consider yourself a pretty lucky person to have made the right decisions to survive until you found safety.")
                        input(f"Congratulations {player}, you earned 5 more points for getting saved. Your point total now meets the threshold to win the game!!!!")
                    print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
                    
                        
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