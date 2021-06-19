# to iterate over the indexes of a list
# for i in range(len(someList))

# use in to check a value is or isn't in a list

myPets = ['zoe', 'pooka', 'fat-tail']

print('enter a pet name:')
name = input()

if name not in myPets:  # if name not in myPets
    print('i do not have a pet named ' + name)
else:                   # if name in myPets
    print(name + ' is my pet.')

# multiple assignment
cat = ['fat', 'black','loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
# cat = ['fat', 'black','loud']
# size, color, disposition = cat
