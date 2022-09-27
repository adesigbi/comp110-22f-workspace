"""Utils comp exercise"""

__author__ = "730572167"


def only_evens(og_list: list[int]) -> list:
    """Returns the even numbers found in a list."""
    i: int = 0 
    new_list: list[int] = list()
    if len(og_list) == 0:
        return new_list
    while i < len(og_list):
        if og_list[i] % 2 == 0:
            new_list.append(og_list[i])
        i += 1
    return new_list


def concat(list_1: list[int], list_2: list[int]) -> list:
    """Concatinates two lists of ints together."""
    i: int = 0 
    new_list: list[int] = list()

    while len(list_1) != 0 and i < len(list_1):
        new_list.append(list_1[i])
        i += 1

    i = 0

    while len(list_2) != 0 and i < len(list_2):
        new_list.append(list_2[i])
        i += 1
    
    return new_list


def sub(a_list: list[int], start_i: int, end_i: int) -> list:
    new_list: list[int] = list()
    i: int = start_i
    
    if i < 0:
        i = 0
    if end_i > len(a_list):
        end_i = len(a_list)
    if len(a_list) == 0 or i > len(a_list) or end_i <= 0:
        return new_list

    while i < end_i:
        new_list.append(a_list[i])
        i += 1
    return new_list

