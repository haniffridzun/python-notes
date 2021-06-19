# dictionary: key-value
birthdays = {'alice': 'apr 1', 'bob': 'dec 12', 'carol': 'mar 4'}

while True:
    print('enter a name: (blank to quit)')
    name = input()
    if name == '':                  # break loop
        break
    if name in birthdays:           # if name in the dictionary
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('i do not have birthday information for ' + name)
        print('what is their birthday?')
        birthdays[name] = input()   # add date to new name in dictionary
        print('birthday database updated.')

# keys()
# values()
# items()

''' items()
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('key: ' + k + ' value: ' + str())
'''
# output:
# key: age value 42
# key: color value red

''' get()
picnicItems = {'apple': 5, 'cups': 2}
print('i am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('i am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
'''
# output:
# i am bringing 2 cups
# i am bringing 0 eggs
