import re

# | character is called a pipe, use to match many expressions
# example: r'batman|tina fey' will match either 'batman' or 'tina fey'
heroRegex = re.compile(r'batman|tina fey')
mo = heroRegex.search('batman and tina fey')
print(mo.group())      # output: batman
# when both occur, first occurence of matching text will be returned as match object

# use pipe to match one of several patterns as part of regex
batRegex = re.compile(r'bat(man|mobile|copter|bat)')
mo = batRegex.search('batmobile lost a wheel')
print(mo.group())      # output: 'batmobile'
print(mo.group(1))     # output: 'mobile'

# optional matching with question mark
# ? regex should find a match whether or not that bit of text is there
batRegex = re.compile(r'bat(wo)?man')
mo1 = batRegex.search('the adventures of batman')
print(mo.group())       # output: 'batman'
mo2 = batRegex.search('the adventures of batwoman')
print(mo2.group())      # output: 'batwoman'

# matching zero or more with asterisk
# group that precedes the asterisk can occur any num of times in text
# can be absent or repeated over
batRegex = re.compile(r'bat(wo)*man')
mo1 = batRegex.search('the adventures of batman')
print(mo1.group())  # output: 'batman'
mo2 = batRegex.search('the adventures of batwoman')
print(mo2.group())  # output: 'batwoman'
mo3 = batRegex.search('the adventures of batwowowoman')
print(mo3.group())  # otuput: 'batwowowoman'

# matching one or more with the plus
# group preceding a plus must appear at least once. not optional
batRegex = re.compile(r'bat(wo)+man')
mo1 = batRegex.search('the adventures of batman')
print(mo1)  # output: 'None'
mo2 = batRegex.search('the adventures of batwoman')
print(mo2.group())  # output: 'batwoman'
mo3 = batRegex.search('the adventures of batwowowoman')
print(mo3.group())  # otuput: 'batwowowoman'

# matching specific repetitions with curly brackets
# (Ha){3} == (Ha)(Ha)(Ha)
# (Ha){3,5} == ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha))
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())  # output: 'HaHaHa'
mo2 = haRegex.search('Ha')
print(mo2)          # output: None
