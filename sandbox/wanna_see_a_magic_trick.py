"""That empty thing"""
do_they_wanna_see_it: str = input("Wanna see a magic trick? ")

if do_they_wanna_see_it == no:
    print("Ok, then good day sir..... or ma'am..or um..... gentle person")
elif do_they_wanna_see_it == No:
    print("Ok. Bye")
elif do_they_wanna_see_it == NO:
    print("I respect your opinion, but that doesn't mean that I don't judge it")
else:
    empty: str = input("Ok, type the word 'empty':")
    index
    while empty == "empty":
        print("That's not the word I told you to type. It's cap sentative, try again")
        input("Press any character to continue")
        empty = input("Type the word 'empty': ")
    input("Press any character to continue: ")
    index: int = len("empty")
    while index >= 0:
        print("[  " + empty + "  ]")  
        empty = empty[:-1]
        index -= 1