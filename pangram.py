# DETERMINES IF PROVIDED STRING IS A PANGRAM (USES EVERY LETTER IN THE ALPHABET
import string
from string import digits


s = "The quick, brown fox jumps over the lazy dog32523!"

"""
def is_pangram(s):
    range = string.ascii_lowercase[:26]   # call the alphabet
    range = list(range)
    string2 = ''.join(filter(str.isalnum, s))   # removes all spaces, punctuation
    remove_digits = str.maketrans('', '', digits)   # removes numbers
    string2 = string2.translate(remove_digits)   # continues to remove numbers
    string2 = [a.lower() for a in string2]   # turns string into all lower case
    string2 = set(list(string2))   # removes duplicates and makes string a list
    print(range)
    print(string2)
    return len(string2) == len(range)   # returns True or False


print(is_pangram(s))
"""

# ---------> ALTERNATIVE THAT SOMEONE SMARTER THAN ME USED
def is_pangram2(s):
    s = s.lower()
    # range = string.ascii_lowercase[:26]
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

print(is_pangram2(s))


def dirReduc(arr):
    dict = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    result = []
    for i in arr:
        # print(dict[i])   # prints the dict value of the key from arr
        print(result)
        if result and dict[i] == result[-1]:
            result.pop()
        else:
            result.append(i)

    return (result)

#print(dirReduc(arr = ['NORTH', 'SOUTH', 'SOUTH', 'WEST', 'EAST', 'NORTH', 'WEST']))
print(dirReduc(arr = ['NORTH', 'SOUTH', 'SOUTH', 'EAST']))
