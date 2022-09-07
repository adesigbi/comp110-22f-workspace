"""One shot world game."""
__author__ = "730572167"

secret_word: str = "python"
number_of_letters: int = len(secret_word)
users_word: str = input(f"What is your {number_of_letters}-letter guess? ")

while len(users_word) != number_of_letters:
    users_word = input(f"That was not {number_of_letters} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
emoji_string: str = ""
letter_in_word: bool = False
i1: int = 0

# does the concatination
while i < len(secret_word):
    # checks to see if the letter the user put is in the secret word
    while i1 < len(secret_word):
        if users_word[i] == secret_word[i1]:
            letter_in_word = True
        i1 += 1
    if users_word[i] == secret_word[i]:
        emoji_string += GREEN_BOX
    elif letter_in_word:
        emoji_string += YELLOW_BOX
    else:
        emoji_string += WHITE_BOX
    i += 1
    i1 = 0
    letter_in_word = False
print(emoji_string)

if users_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")