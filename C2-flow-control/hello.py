# this program says hello and asks for my name.
print('hello world!')
print('what is your name?')
# save input into variable myName
myName = input()
print('it is good to mee tyou, ' + myName)
print('the length of your name is:')
# len() function - evaluates number of character in that string
print(len(myName))
print('what is your age?')
# save input into variable myAge
myAge = input() # input() function always returns a string, even if user enters number
# str() function - concatenate int with string
print('you will be ' + str(int(myAge) + 1) + ' in a year.')
