"""A ship wreck choose your own adventure game."""


__author__ = "730572167"

from random import randint
points: int = 0 
player: str = ""
playing: bool = True
SHIP_EMOJI: str = "\U0001F6F3"


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
    """Checks if a word is in a list and returns a bool."""
    for item in list:
        if item == word:
            return True
    return False


def word_finder(word: str, list: list[str]) -> str:
    """Sees if a given word is a part of a given list and returns that word if it is.""" 
    while not word_in_list(word, list):
        word = input("Sorry, the item you typed is not in the list. Recheck your spelling and try again: ")
    return word
        

def index_finder(word: str, list: list[str]) -> int:
    """Finds the index of a given word in a list."""
    i: int = 0 
    while i < len(list):
        if word == list[i]:
            return i
        i += 1


def take_from_list(item_list: list[str]) -> None:
    """Prompts the player to take 4 items from a list."""
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
    player = input("Welcome to the game. What is your name?: ")
    input(f"Hi {player}, Welcome to shipwreck survival {SHIP_EMOJI}. Your goal (as the title of the game may suggest) is to survive a shipwreck and be rescued.\n"
          "This is indicative of earning 25 points, so the closer you are to that number, the closer you are to winning. Here’s the scenario: You are on a sinking cruise ship.\n"
          "You just caught sight of the captain doing the cross before hopping into a specially made life raft. You run up to the upper deck and see that there are two life rafts\n"
          "that you can choose from. You have no information about either rafts other than the fact that though both rafts\n"
          "should contain the materials for one to survive and be rescued within 10 days, the exact materials on the rafts vary slightly.\n"
          "Press enter to continue through the rest of these prompts: ")


def stop_game() -> None:
    """Stops the game and gives player their points."""
    global playing 
    playing = False
    print(f"Goodbye {player}. In your last experience, you gathered {points} adventure points. We hope you come to play again soon! ")
   

def boat1() -> None:
    """Actions happening given the user picks the first boat."""
    global points 
    item_list1: list[str] = ["first aid kit", "battery powered radio", "compass", "army rations", "shaving mirror", "tent", "matches", "plastic bags"]
    input("\nIn a rush, you board the first life raft. And by rummaging through the back of the raft, you find the following items\n")
    for i in item_list1:
        print(i)
    input("**Keep in mind that the tent is perfectly made for the raft, and is not capable of being used for anything else \n")
    input("\nNow before you boarded the life raft, between gently sobbing and hopping into a boat, the last man working on the ship, gave a cryptic message explaining that \n"
          "the rafts are old so that if you were to keep all items on the ship, you would definitely drown. He said that you’d probably be safe if you only kept 4 of the items: \n")
    take_from_list(item_list1)
    points += 2
    input(f"Congrats {player}, you have completed your first task, and by doing so, you have earned 2 points. Your new point total is now {points}. ")
    input("\n==========That Night==========\n")
    appropriate_materials1: bool = word_in_list("tent", item_list1)
    if not appropriate_materials1:
        input("It starts drizzling when you go to sleep. You hope that it doesn’t get worse because you don’t have the materials to protect yourself from the rain.")
        input("The weather gets worse and you are left shivering through the night. ")
        input("Uhoh, you've died of hypothermia :( ")
        input("You were never saved. ")
        print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
        return
    if appropriate_materials1:
        rain_response: str = input("It starts to drizzle outside. You realize that you have the materials to protect youself if the rain gets worse but, you don't really have the energy to.\n"
                                   "Do you want to protect yourself from the rain or save energy and worry about shelter tomorrow? Type 'save energy' or 'protect from rain': ")
        rain_response = valid_word2(rain_response, "save energy", "protect from rain")
        if rain_response == "save energy":
            input("You soon hear thunderstorms. You try to sleep through the rain. ")
            input("The weather gets worse and you are left shivering through the night. ")
            input("Uhoh, you've died of hypothermia. ")
            input("You were never saved. ")
            points += 1
            print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
            return
        if rain_response == "protect from rain":
            input("You use your tent to build shelter and do so just in the nick of time. The storm reaches its head when you head inside.\n"
                  "You would have surely died of hypothermia if you had decided to sleep exposed to the elements. ")
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
                points += 1
                input(f"You try to muster together a water collection system with your {water_collector} and go off to sleep.\n")
                input("In the morning, you see that your system has completely failed")
                input("\n=====Day 2=====\n")
                input("The thirst and dissapointment from your past actions starts settling in.")
                input("\n=====Day 3=====\n")
                input("You understand your fate and in vain, take in mouthfulls of ocean water, hoping that what all those 'scientists' say about osmosis and salt was wrong. \nYou promptly vomit and within the hour, start to hallucinate.")
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
                if not word_in_list("army rations", item_list1):
                    input("Oh no, it looks like there is no food in the items that you originally chose. \n")
                    input("\n=====Day 5=====\n")
                    input("You have gone 5 days without food and you think that the hunger is subsiding. \n"
                          "You continue your daily rituals and make sure your water collection system is still working well.")
                    input("\n=====Day 6=====\n")
                    input("You are craving something to eat again. Delirious and disappointed in your past decisions, you try catching fish. \n"
                          "In an attempt to grab a salmon with your bare hands, you fall overboard.")
                    input("Sorry, you died from drowning and hunger. ")
                    input("You were never saved.")
                    print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
                    return 
                if word_in_list("army rations", item_list1): 
                    input("You start tearing into your army rations and begin to create rituals to maintain your survival.\n"
                          "You wake in the morning, pack up your tent to conserve space, have the breakfast of champions that is canned meats and stale bread,\n"
                          "tinker with your objects on your person to try to make tools, eat dinner a of canned beans and crackers, set up up your tent again,\n"
                          "sleep, and do the same thing over again. You have all your basic necessities covered.")
                    points += 5
                    input(f"\nCongratulations {player}, you had a viable food source and gain 5 more points. You have a total of {points} points. ")
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
                        points += 1
                        if ending == 1:
                            input("You have become accustomed to being on the raft and live your best seafaring life. You figured out how to catch fish and turtles for food. \n"
                                  "You've even made some hats from their shells.")
                            input("You die at the age of 60, having never seen a human being again. ")
                            input("Did you win? Most wouldn't say so. But in your heart, on your death raft aged and wise, you thought 'surely I did.'")
                            input("You were never saved")
                        if ending == 2:
                            input("On day 14, you fought a losing battle with a hord of sharks. In the throws of action with the sea creatures, you thought that it was probably niave to think\n"
                                  "that you'd survive months on the atlantic scratch free. That would require some great stroke of luck. Another boat came back around on the 24th day.")
                            input("You were never saved")
                        if ending == 3:
                            input("On the 24th day, another boat would come by, this time within yelling distance of your raft. Unfortunately, on your 23rd day you slept walked off of the raft.\n")
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
                        points += 3
                        input("You will tell your accolades to family and strangers alike and sue the cruise line involved in the sinking of your vessel, gaining a fortune in the process.")
                        input("Though a pretty unfortunate event happened to you, you consider yourself a pretty lucky person to have made the right decisions to survive until you found safety.")
                        input(f"Congratulations {player}, you earned 5 more for doing using the correct device and 3 bonus points for surviving until rescue. You've earned enough points to win the game!!!!")
                    print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")


def boat2(points: int) -> None:
    """Actions that happen after the user picks the second boat."""
    item_list2: list[str] = ["pocket knife", "map of the atlantic", "compass", "fishing kit", "a bucket", "tarp and sleeping bag", "rubbing alcohol", "petroleum/oil mixture"]
    input("\nWithout much thinking, you chose the second life raft. And by rummaging through the back of the raft, you find the following items\n")
    for i in item_list2:
        print(i)
    input("**Keep in mind that petroleum/oil mixture also comes with matches. It is also not capable of being used for cooking or powering the raft. \n")
    input("\nNow before you boarded the life raft, between gently sobbing and hopping into a boat, the last man working on the ship, gave a cryptic message explaining that \n"
          "the rafts are old so that if you were to keep all items on the ship, you would definitely drown. He said that you’d probably be safe if you only kept 4 of the items. ")
    take_from_list(item_list2)
    points += 2
    input(f"Congrats {player}, you have completed your first task, and by doing so, you have earned 2 points. Your new point total is now {points}\n")
    input("Uhoh it looks like raft 2 contains packs of uncooked steaks below the deck. You become aware of this fact when sharks start to circle around you. ")
    input("You try all the tricks in the book. You play dead, you make loud noises, you try to move away without making much movement,\n"
          "but the sharks don’t leave. In fact, it seems that even more are coming. ")
    input("A single shark in the crowd leads the force. And as it approaches, you close your eyes and hope for the best. ")
    shark_survival: int = randint(1, 100)
    shark_survival = 1
    previous_score: int = points
    for i in item_list2:
        if (i == "fishing kit") or (i == "a bucket") or (i == "tarp and sleeping bag") or (i == "petroleum/oil mixture"):
            points += 5
    shark_msg: str = ""
    if not word_in_list("tarp and sleeping bag", item_list2):
        shark_msg += "Hypothermia, because you didn’t have anything to protect you from the elements when it"
    if not word_in_list("a bucket", item_list2):
        shark_msg += "\nDehydration, because you didn’t have any materials to gather water when it rained"
    if not word_in_list("fishing kit", item_list2):
        shark_msg += "\nStarvation, because you didn’t have any device to obtain food" 
    if not word_in_list("petroleum/oil mixture", item_list2):
        shark_msg += "\nLack of rescue, because you didn’t have anything that could be used to signal to other ships from far away"
    if shark_survival == 1:
        input(f"\nCongratulations {player}. You miraculously survived the attack by some combination of nose punches and eye gauges. That truly had a 1 in 100 chance of happening!!!")
        if points != 22:
            input("Unfortunately, though, you didn’t have the proper materials to survive and be rescued.\n"
                  "You died due to one or more of the following...")
            input(shark_msg + " ")
            input(f"This makes your point total {points} (with +5 points for every correct item and action in survival and rescue added on to your previous score of {previous_score})")
        if points == 22:
            points += 3
            input("You also had the right materials to survive and be rescued. ")
            input("First, you made shelter with your tarp and sleeping bag protecting you from the rain. ")
            input("You then started fishing and began to stave off dehydration with rain water you gathered from your bucket and turtle blood you drink from (well) turtles.")
            input("And lastly, you signaled for help with your petroleum oil mixture. ")
            input("\n======Some time in the future=======\n")
            input("You went down in history with your survival, signed a book deal, and later turned your experience into a movie called “Jaws, but not that one”.")
            input(f"You gained {points} points from having the materials to complete all 4 basics of survival at sea: shelter (to prevent hypothermia), water, food, and rescue.\n"
                  "For each of these actions you received 5 points and you gained 3 more bonus points for surviving to tell the tale.\n You win!!!!!")
    if shark_survival != 1:
        input("\nYou died of a shark attack. ")
        if points != 22:
            input("But hey, you didn’t have the proper materials to survive until rescue anyways.\n"
                  "You would have died due to…")
            input(shark_msg + " ")
            input(f"This makes your point total {points} (with +5 points for every correct item and action in survival and rescue added on to your previous score of {previous_score})")
        if points == 22:
            input("But at least you had the right idea, because all of the items you kept were indicative of your success on the waters. ")
            input(f"This makes your point total {points} (with +5 points for every correct item and action in survival and rescue added on to your previous score of {previous_score}).\n"
                  "You lost, but you were only 3 points away from winning the game. All you had to do was beat the one in a hundred odds of surviving a shark attack.")
    return points
 

def main() -> None:
    """Main function that everything goes through."""
    greet()
    global points
    # present the user with three optionn
    while playing:
        first_branch: str = input("Choose either boat 1 or boat 2 by typing “boat 1” or “boat 2”. If you do not want to continue playing the game, type “leave game”. ")   
        first_branch = valid_word3(first_branch, "boat 1", "boat 2", "leave game")
        
        if first_branch == "boat 1":
            # run boat1 (interacts directly with global point values)
            points = 0 
            boat1()
        elif first_branch == "boat 2":
            # run boat2- shark infested waters
            points = 0 
            points = boat2(points)
            print(f"\n\n========Game Over=========\n\nIn your experience, you earned {points} points.")
        elif first_branch == "leave game":
            # stop the program, summed adventure points
            stop_game()
            return
        input("\nDo you want to play again? Do you want to exit? Press enter to continue either way. ")


if __name__ == "__main__":
    main()