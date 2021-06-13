import random # import random module from standard library
def getAns(ansNum):
    if ansNum == 1:
        return 'it is certain' # specify what the return value should be 
    elif ansNum == 2:
        return 'it is decidely so'
    elif ansNum == 3:
        return 'yes'
    elif ansNum == 4:
        return 'reply hazy try again'
    elif ansNum == 5:
        return 'ask again later'
    elif ansNum == 6:
        return 'concentrate and ask again'
    elif ansNum == 7:
        return 'my reply is no'
    elif ansNum == 8:
        return 'outlook not so good'
    elif ansNum == 9:
        return 'very doubtful'

r = random.randint(1, 9)
fortune = getAns(r)
print(fortune)
# print(getAns(random.randint(1, 9)))

print('hello') # print() function automatically adds a newline
print('world')
# output:
# hello
# world

print('hello', end='') # disable newline using end keyword
print('world')
# otuput: helloworld

# pass multiple string values to prints
print('cat','dogs','mice') # print() function automatically separate them with single space
# output: cats dogs mice

print('cats','dogs','mice', sep=',') # remove separation using sep keyword
# output: cats,dogs,mice
