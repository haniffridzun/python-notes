'''
\d :: any numeric digit from 0 to 9

\D :: any char that is not a numeric digit

\w :: any letter, numeric digit, or underscore char

\W :: any char that is not letter, numeric, or underscore

\s :: any space, tab or newline char

\S :: any char that is not space, tab or newline
'''
import re

# regex \d+\s\w+ will match text that has one or more numeric,
# followed by a whitespace
# followed by one or more letter/digit/underscore char
xmasRegex = re.compile(r'\d+\s\w+')
cc = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(cc)


# making your own character classes
# example :: [a-zA-Z0-9] will match all lowercase, uppercase letters and num
vowelRegex = re.compile(r'[aeiouAEIOU]')
vo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD')
print(vo)

consonantRegex = re.compile(r'[^aeiouAEIOU]')   # ^ make a negative char class
co = consonantRegex.findall('RoboCop eats baby food. BABY FOOD')
print(co)


# caret (^) at start of regex  to indicate that a match must occur at beginning
beginsWithHello = re.compile(r'^Hello')
begins = beginsWithHello.search('Hello world!')
print(begins)

# dollar ($) at the end of regex to indicate the string must end with this pattern
endsWithNum = re.compile(r'\d$')
ends = endsWithNum.search('your number is 19')
print(ends)

# both begin and end
wholeStrIsNum = re.compile(r'^\d+$')
whole = wholeStrIsNum.search('123455673')
print(whole)

