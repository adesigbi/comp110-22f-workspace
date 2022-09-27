"""An example of conditional (if-else) statements."""
from tkinter.messagebox import YES


SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET: 
        print("Guess a bit lower")
    

print("Game over.")