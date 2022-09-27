"""An exmaple of a while loop statment."""

counter: int =  0 
maximum: int = int(input("What number do you want me to count to?: "))
while counter - 1 < maximum:
    print("The square of " + str(counter) + " is " + str(counter ** 2))
    counter = counter + 1
print("Done!")