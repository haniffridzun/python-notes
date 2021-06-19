'''
escape characters
\' :: single quote
\" :: double quote
\t :: tab
\n :: newline or line break
\\ :: backslash
'''

# raw strings :: ignores all escape characters
# print(r'that is carol\'s cat.')
# output: that is carol\'s cat

print('''dear alice,
eve's cat has been arrested for catnapping, cat burglary and extortion.
sincerely,
bob''')
# output:
#dear alice,
#eve's cat has been arrested for catnapping, cat burglary and extortion.
#sincerely,
#bob
