"""While loop checking if character is in a word"""
word: str = input("Type a word: ")
character: str = input("Type a character: ")

index: int = 0 
number_of_instances: int = 0 

while index < len(word):
    if word[index] == character:
        number_of_instances += 1
        print(character + " found out index " + str(index))
    index += 1 
print(str(number_of_instances) + " instances of " + character + " found in " + word)
    