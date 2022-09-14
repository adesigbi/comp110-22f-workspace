"""Structured wordle things."""
__author__ = "730572167"


def contains_char(secret: str, character: str) -> bool:
    """Lets know if your character is in the string."""
    assert len(character) == 1
    i: int = 0 
    while i < len(secret):
        if secret[i] == character:
            return True
        i += 1
    return False    


def emojified(guess: str, secret: str) -> str:
    """Uses contains_char to see what spot a character is found."""
    assert len(guess) == len(secret)
    i: int = 0 
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    them_boxes: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            them_boxes += GREEN_BOX
        elif contains_char(secret, guess[i]):
            them_boxes += YELLOW_BOX
        else:
            them_boxes += WHITE_BOX
        i += 1
    return them_boxes


def input_guess(expected_length: int) -> str:
    """Ask you to type a letter with the expected lenght of characters."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 1
    playing: bool = True
    while turns < 7 and playing:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            playing = False
            print(f"You won in {turns}/6 turns!")
        turns += 1
    if guess != secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()