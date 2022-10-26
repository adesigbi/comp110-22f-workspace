"""Pratice from class (for in)"""


def zip(keys: list[str], values: list[str]) -> dict[str, str]:
    assert len(keys) == len(values)
    new_dict: dict[str, str] = dict()
    i: int = 0 
    for key in keys:
        new_dict[key] = values[i]
        i += 1
    return new_dict

list_1: list[str] = ["tom", "jerr", "asd", "the world"]
list_2: list[str] = ["a", "b", "c", "d"]

print(zip(list_1, list_2))


def odd_and_evens( list_of_nums: list[int]) -> list[int]:
    odd_and_even_list: list[int] = []
    for i in range (0, len(list_of_nums), 2):
        if list_of_nums[i] % 2 == 1:
            odd_and_even_list.append(list_of_nums[i])
    return odd_and_even_list

print(odd_and_evens([2, 3, 4, 5, 6, 7, 81, 2, 4, 9, 11]))



def vowels_and_threes(user_str: str) -> str:
    vowel_3_str: str = ""
    i: int = 0 
    for chr in user_str:
        vowel_in_str: bool = False
        divis_3: bool = False
        continu: str = "y"
        vowel_list: list[str] = ["a", "e", "i", "o", "u"]
        if chr in vowel_list:
            vowel_in_str = True
        if i % 3 == 0:
            divis_3 = True
        if vowel_in_str and divis_3:
            continu = "n"
        if continu == "y":
            if vowel_in_str or divis_3:
                vowel_3_str += chr
        i += 1
    return vowel_3_str 

def vowel_and_threes2(user_string: str) -> str:
    new_string: str = ""
    vowel_in_string: bool = False
    vowel_list: list[str] = ["a", "e", "i", "o", "u"]
    i: int = 0 
    while i < len(user_string):
        vowel_in_string = False
        for vowel in vowel_list:
            if i == vowel:
                vowel_in_string = True
        if vowel_in_string and i % 3 == 0:
            new_string += ""
        elif vowel_in_string or i % 3 == 0:
            new_string += user_string[i]
        i += 1
    return new_string



def vowel_and_threes3(og_string: str) -> str:
    """Given a string returns a new string containing the characters either at index divisible by 3, or a vowel (but not both)"""
    new_string: str = ""
    vowel_list: list[str] = ["a", "e", "i", "o", "u"]
    vowel_in_string: bool = False
    i: int = 0 
    while i < len(og_string):
        vowel_in_string = False
        for vowel in vowel_list: 
            if vowel == og_string[i]:
                vowel_in_string = True
        if vowel_in_string and i % 3 == 0:
            new_string += ""
        else:
            if vowel_in_string or i % 3 == 0:
                new_string += og_string[i]
        i += 1
    return new_string


print(vowel_and_threes3(["a", "e", "i", "o", "u", "l"]))

def odd_and_even2(og_list: list[int]) -> list:
    """takes in a list and returns one with numbers that are odd andd have an even idnex"""
    new_list: list[int] = []
    for i in range(0, len(og_list), 2):
        if og_list[i] % 2 == 1:
            new_list.append(og_list[i])
    return new_list

print(odd_and_even2([2, 3, 4, 5, 6, 7, 81, 2, 4, 9, 11]))















def odd_and_even3(og_list: list) -> list:
    """takes in list, returns list that is even index"""
    new_list: list[int] = []
    i: int = 0 
    while i < len(og_list):
        if i % 2 == 0 and og_list[i] % 2 == 1:
            new_list.append(og_list[i])
    return new_list


print(odd_and_even2([2, 9, 4, 17, 9, 10, 15, 13, 14, 23]))

def column_taker(list_of_dicts: list[dict[str, str]], column: str) -> list[str]:
    column_values_list: list[str] = []
    for dict in list_of_dicts: 
        if column in dict: 
            column_values_list.append(dict[column])
    return column_values_list


def zip1(keys: list[str], values: list[str]) -> dict[str, str]:
    assert len(keys) == len(values)
    new_dict: dict[str, str] = {}
    for i in range(0, len(keys), 1):
        new_dict[keys[i]] = values[i]
    return new_dict


def average_grades2(grades: dict[str, int]) -> dict[str, float]:
    averaged_grades: dict[str, float] = {}
    for name in grades:
        grade_list: list[int] = grades[name]
        sum: int = 0 
        for number in grade_list:
            sum += number
        averaged_grades[name] = sum/len(grade_list)
    return averaged_grades



def read_lines(filename: str) -> list[str]:
    lines: list[str] = []
    opened_file = open(filename, "r")
    for line in opened_file:
        lines.append(line)
    return lines


