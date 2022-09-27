"""Example of looping trhough all characters in a string"""

user_string: str = input("Type a string: ")
# The varaible i is a common counter variable in programing
i: int = 0
while i < len(user_string):
    print(user_string[i])
    i = i + 1
print("Done! ")