# all regex functions in python are in re module
import re

# create regex pbject that matches the phone num pattern
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# r'string' is alternative to escape char '\'
# adding parenthesis will create groups in the regex (\d\d\d)

# mathcing regex objects
mo = phoneNumRegex.search('my number is 415-555-4242.')
# search() method will return None if the regex pattern is not found
# returns Match object if pattern is found

print('phone number found: ' + mo.group())
# group() method will return the actual matched pattern
# output: phone number found: 415-555-4242

# 1st group
mo.group(1)     # '415'
# 2nd group
mo.group(2)     # '555-4242'
# no group
mo.group(0)     # '415-555-4242'
mo.group()

# groups() returns tuple of multiple values
areaCode, mainNum = mo.groups()     # use multiple assignment to assign each value to a separate variable
print(areaCode)
print(mainNum)
