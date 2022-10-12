"""Some practice with dictionaries."""


__author__: "730572167"

def invert(og_dict: dict[str, str]) -> dict[str, str]:
    """Inverts values and keys in a dictionary."""
    new_dict: dict[str, str] = {}
    # if one value == another value in dictionary -> KeyError
    for i1 in og_dict:
        # if item i1 is equal to more than one of any of the other items in dict
        duplicate_values: int = 0 
        for i2 in og_dict:
            if og_dict[i1] == og_dict[i2]:
                duplicate_values += 1
        if duplicate_values > 1:
            raise KeyError
    for old_key in og_dict:
        old_value: str = og_dict[old_key]
        # new_key is equal to old value
        new_key: str = old_value
        # value is equal to old key
        new_value: str = old_key
        new_dict[new_key] = new_value
    return new_dict


def favorite_color(fav_color_dict: dict[str, str]) -> str:
    """Finds the most common favorite color."""
    color_repeats_to_beat: int = 0 
    i: int = 0 
    # sees if color is other values
    for key1 in fav_color_dict:
        # makes first item of dictionary the color mode
        if i == 0:
            color_mode = fav_color_dict[key1]
        current_color_repeats: int = 0 
        # if a current value is seen, adds to current color repeats
        for key2 in fav_color_dict:
            if fav_color_dict[key1] == fav_color_dict[key2]:
                current_color_repeats += 1  
        # if current_color_repeat is greater than color_repeats_to_beat, the new mode becomes the color associated with the key your working on the and current_color_repeats becomes color_repeats_to_beat
        if current_color_repeats > color_repeats_to_beat:
            color_mode = fav_color_dict[key1]  
            color_repeats_to_beat = current_color_repeats
        i += 1
    return color_mode


def count(old_list: list[str]) -> dict[str, int]:
    new_dict: dict[str, int] = {}
    for item in old_list:
        # for every item in the list, add it as a key in the new dict
        # if the item is already present, make the value += 1
        if item in new_dict:
            new_dict[item] += 1
        if item not in new_dict:
            new_dict[item] = 1
    return new_dict

       
        


    

