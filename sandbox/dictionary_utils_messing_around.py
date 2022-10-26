"""Messing around with those dictionary utils (doing them in different ways)"""


from nbformat import current_nbformat


def invert(old_dict: dict[str, str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}
    # when in loop (before added to dictionary), if str is in value already, raise error
    for key in old_dict:
        new_key: str = old_dict[key]
        new_value: str = key
        if new_key in new_dict:
            raise KeyError
        new_dict[new_key] = new_value
    return new_dict

print(invert({'a': 'z', 'b': 'y', 'c': 'x'}))
print(invert({'yellow': 'yellow', 'red': 'red'}))
print("something evaluated")


def favorite_color(color_list: dict[str, str]) -> str:
    """Finds the color with the greatest frequency."""
    mode_color: str = ""
    frequency_to_beat: int = 0
    for name1 in color_list:
        current_frequency: int = 0 
        for name2 in color_list:
            if name1 == name2:
                current_frequency += 1
        if current_frequency > frequency_to_beat:
            mode_color = color_list[name1]             
    return mode_color


print(favorite_color({"John": "green", "Hank": "green", "lauri": "pink", "tommy": "pink", "Mark": "pink"}))
print(favorite_color())