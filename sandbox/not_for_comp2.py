"""Password checker (to see if you have the necessary digits)"""
user_password: str = input("Write a password that contains atleast 1 lowercase letter between a-g, 1 number, and 1 special character: ")

index: int = 0 
password_lacks_number: bool = True

#number finder 
#if no numbers were found, number becomes false
#(password_contains_number == False) or

while password_lacks_number and index < len(user_password):
    if user_password[index] == ("1" or "2"):# or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"):
        password_lacks_number = False
    else:
       index += 1

password_lacks_character: bool = True 
index = 0
while password_lacks_character and index < len(user_password):
    if user_password[index] == ("a" or "b"): #or "c" or "d" or "e" or "f" or "g"):
        password_lacks_character = False
    else:
        index += 1


if password_lacks_number == True:
    print("Your pasword lacks a number") 
if password_lacks_character == True:
    print("Your password lacks a lowercase letter between a-g")
if (password_lacks_number or password_lacks_character) == False:
    print("Your password fuffils all of the requirements!")  
 