import re
# python's regexs are greedy by default
# in ambiguous situations they will match longest string possible

# greedy matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHa')
print(mo1.group())      # output: HaHaHaHaHa

# non greedy matching
# matches shortest string possible
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')    # followed by question mark
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())      # output: HaHaHa


# findall() method - willnot return Match object but a list of strings
# as long as there are no groups in regex
# if there are groups in regex, then findall() will return a list of tuples
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # has no groups
fo = phoneNumRegex.findall('cell: 415-555-9999 work: 212-555-0000')
print(fo)               # output: ['415-555-9999', '212-555-0000']

