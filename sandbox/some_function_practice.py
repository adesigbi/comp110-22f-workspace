"""Write a python function to find the Max of three numbers"""


def max(n1: int, n2: int, n3: int) -> int:
    if n1 < n2 and n3 < n2:
        return n2
    elif n2 < n1 and n3 < n1:
        return n1
    else:
        return n3


def sum(numbers) -> int:
    """Find the sum of a list"""
    i: int = 0
    list_sum: int = 0
    while i < len(list):
        list_sum += list[i]
        i += 1
    return list_sum


def times_things(them_lines: list[int]) -> int:
    """Multiplies a list together"""
    i: int = 0
    product: int = 1 
    int(them_lines)
    while i < len(them_lines):
        product *= them_lines[i]
        i += 1


def int_converter(them_lines: list[str]) -> None:
    """converts inputed list of strings into a list of ints"""
    i: int = 0 
    while i < len(them_lines):
        them_lines[i] = int(them_lines[i])
        i = i + 1



my_list: input("Write a list: ")

print(type(my_list))


#Ask the person to input a list and I will find the product of the numbers



