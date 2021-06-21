import re

# . char in regex is called wildcard
# it will match any char and just one char except for a newline
atRegex = re.compile(r'.at')
ato = atRegex.findall('the cat in the hat sat on the flat mat.')
print(ato)          # output: ['cat', 'hat', 'sat', 'lat', 'mat']


# matching everything with dot-star
# * char means zero or more of preceding char
nameRegex = re.compile(r'first name: (.*) last name: (.*)')
mo = nameRegex.search('first name: al last name: sweigart')
print(mo.group(1))  # output: al
print(mo.group(2))  # output: sweigart

# dot-star uses greedy mode: it will always try to match as much text
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())   # output: <To serve man> for dinner.>
# to match any and all text in nongreedy fashion use .*?
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())   # output: <To serve man>

# matching newlines with dot char
# passing re.DOTALL as 2nd argument to re.compile
newlineRegex = re.compile('.*', re.DOTALL)
no = newlineRegex.search('serve the public trust.\nprotect the innnocent.\nuphold the law.').group()
print(no)
'''
output:
serve the public trust.
protect the innnocent.
uphold the law.
'''
