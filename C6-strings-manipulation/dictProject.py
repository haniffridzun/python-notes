'''
create a fantasy video game. the data structure to model the player's
inventory will be a dictionary where the kyes are string values describing
the item in the inventory and the value is an integer value detailing how
many of that item the player has. Example, rope:1, torch:6, gold coin:42,
dagger:1, arrow:12

write a function named displayInventory() that would take any possible
inventory and display it like following:
inventory:
12 arrow
42 gold coin
1 rope
total number of items: 55

hint: you can use a for loop to loop through all keys in dictionary
'''

# dictionary for inventory
stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

# function for displayInventory()
def displayInventory(inventory):
    print('inventory:')
    item_total = 0
    for k, v in inventory.items():      # give tuples of key and values
        print(str(v) + ' ' + k)         # print value and key each loop
        item_total = item_total + v     # sum all items each loop
    print('total number of items: ' + str(item_total))

displayInventory(stuff)

'''
imagine dragon's loot is represented as list of strings like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
write a function named addToInventory(inventory, addedItems), where
the inventory parameter is a dictionary representing the player's
inventory and the addedItems parameter is a list like dragonLoot.
the addToInventory() function should return a dictionary that represent
the updated inventory. note that the addedITems list can contain multiples
of the same item.
'''
def addToInventory(inventory, addedItems):
    for i in addedItems:                # addedItems is a list
        inventory.setdefault(i, 0)      # for item not in inventory yet will set to default value 0
        inventory[i] += 1               # for item in inventory will add 1 each loop
    return inventory
    

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv,dragonLoot)
# print(inv) check if addToInventory() give dictionary as output
displayInventory(inv)
