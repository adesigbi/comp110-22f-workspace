"""Makes a tuple from a user's input"""



def contains_interger(x: str) -> bool:
    if x == "1" #or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0":
        return True
    else:
        return False


def contains_str(x: str) -> bool: 
    if x != "(" or ")" or "," or " ":
        return True
    else:
        return False

# new_tuple: tuple = ()
# old_tuple: str = input("Write a tuple: ")

# for i in old_tuple:
#     if contains_interger(i) == True:
#         i = int(i)
#         new_tuple += (i)
#     elif contains_str(i) == True:
#         i = i 
#         new_tuple += (i)

# print(new_tuple)   









NewTupleType: tuple = tuple[int, int, str]

color: NewTupleType = (1, 2, "a")

# print(f"print color tuple: {color}" )

# print(f"first index of color tuple {color[1]}")

# print(f"NewTupleType {NewTupleType}")

# print(f"First index of NewTupleType {NewTupleType[1]}")

# print(f"Type of first index of NewTypleType: {type(NewTupleType[1])} ")