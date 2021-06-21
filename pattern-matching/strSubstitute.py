import re

# substitute new text in place of those patterns
# sub() method takes 2 arguments, string to replcace and regex
namesRegex = re.compile(r'Agent \w+')
no = namesRegex.sub('CENSORED', 'Agent alice gave the secret documents to Agent bob.')
print(no)   # output: CENSORED gave the secret documents to CENSORED.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
ao = agentNamesRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(ao)   # output: A*** told C*** that E*** knew B*** was a double agent.
