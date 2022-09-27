"""An eample of a list utility algorithm"""

#Name- contains
# A function with 2 parameters: 
# needle- hat we're searchign for 
#haystack - what we're searching through
#return type: bool
#start from first index
#loop through each index of list
#   test if equal to needle
#       Yes! Return True
#Return False


def contains(needle: str, haystack:list[str]) -> bool:
    i: int = 0 
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i += 1
    return False

print(contains("yo", ["hello", "world", "how", "you", "doin"]))