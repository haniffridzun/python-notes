catNames = [] # use single variable that contains a list value
while True:
    print('enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

# loop ends and print cat names
print('cat names are:')
for name in catNames:
    print(' ' + name)

'''
output
enter the name of cat 1 (or enter nothing to stop)
name 1
enter the name of cat 2 (or enter nothing to stop)
name 2
enter the name of cat 2 (or enter nothing to stop)

cat names are:
 name 1
 name 2
'''
