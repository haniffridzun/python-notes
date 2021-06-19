# nested dictionaries and lists

allGuests = {'alice': {'apples': 5, 'pretzels': 12},
             'bob': {'sandwiches': 3, 'apples': 2},
             'carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, thing):
    numBrought = 0
    for k, v in guests.items():     # k for keys, v for values
        numBrought = numBrought + v.get(thing, 0)
    return numBrought

print('number of things being brought:')
print(' Apples ' + str(totalBrought(allGuests, 'apples')))
print(' cups ' + str(totalBrought(allGuests, 'cups')))
print(' cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' sandwiches ' + str(totalBrought(allGuests, 'sandwiches')))
print(' apple pies ' + str(totalBrought(allGuests, 'apple pies')))
