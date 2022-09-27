"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730572167"
instances_of_character: int = 0
chardle_word: str = input("Enter a 5-character word: ")
if len(chardle_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
chardle_character: str= input("Enter a single character: ")
print("Searching for " + chardle_character + " in " + chardle_word)
if chardle_character == chardle_word [0]:
    print(chardle_character + " found at index 0")
    instances_of_character = instances_of_character + 1
if chardle_character == chardle_word [1]:
    print(chardle_character + " found at index 1")
    instances_of_character = instances_of_character + 1      
if chardle_character == chardle_word [2]:
    print(chardle_character + " found at index 2") 
    instances_of_character = instances_of_character + 1
if chardle_character == chardle_word [3]:
    print(chardle_character + " found at index 3") 
    instances_of_character = instances_of_character + 1
if chardle_character == chardle_word [4]:
    print(chardle_character + " found at index 4") 
    instances_of_character = instances_of_character + 1 
if instances_of_character == 0:
    print("No instances of " + chardle_character + " found in " + chardle_word)
if instances_of_character == 1:
    print(str(instances_of_character) + " instance of " + chardle_character + " was found in " + chardle_word)
if instances_of_character > 1:
    print(str(instances_of_character) + " instances of " + chardle_character + " were found in " + chardle_word)    