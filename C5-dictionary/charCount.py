import pprint

# setdefualt() method
message = 'it was a bright cold day in April, and the clocks were striking thirteen'
count = {}      # empty dictionary

for char in message:
    count.setdefault(char, 0)         # set default count for the character to 0
    count[char] = count[char] + 1     # add 1 each time encounter with the char

print(count)

'''
output:
{'i': 7, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3,'b': 1,
'r': 5,'g': 2, 'h': 3, 'c': 3, 'o': 2,'l': 3, 'd': 3,
'y': 1, 'n': 4,'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2}
'''

# import pprint at top
# pprint() function will pretty print a dictionary's values
pprint.pprint(count)
'''
output:
{' ': 13,
 ',': 1,
 'A': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 7,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
'''
