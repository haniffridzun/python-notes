'''
write a function that takes a list value as an argument and returns a string
with all the items separated by comma and a space, with and inserted before
the last item.

example: spam = ['apples', 'bananas', 'tofu', 'cats']

passing spam list to the function would return
                'apples, bananas, tofu, and cats'.
but your function should be able to work with any list value passed to it.
'''

def commaCode(theList):
    for i in range(len(theList) -1):
        print(theList[i], end=', ')
    print('and ' + theList[-1])


spam = ['apples', 'bananas', 'tofu', 'cats']        
num = ['a', 'b', 'c']
commaCode(spam)
commaCode(num)
