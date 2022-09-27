"""A group of mathmeatical functions"""

def square_root(num: int) -> float:
    num **= .5
    return num

def x_root(num: int, root: int) -> float:
    num **= (1/root)
    return num

