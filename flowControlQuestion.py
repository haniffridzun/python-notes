# Q1: two values of Boolean data type?
# ans: True / False

# Q2: 3 Boolean operators?
# ans: and / or / not

# write code that prints Hello if 1 is stored in spam
# prints Howdy if 2 is stored in spam,
# prints Greetings! if anything else is stored in spam
proceed = ''
while proceed != 'n':
    print('enter positive int')
    spam = int(input())
    if spam == 1:
        print('hello')
    elif spam == 2:
        print('howdy')
    else:
        print('greetings!')
        break

# difference between range(10), range(0, 10), range(0, 10, 1) in for loop?
for i in range(10):
    print(i)    # output: 0,1,2,3,4,5,6,7,8,9

for i in range(0,10):
    print(i)    # output: 0,1,2,3,4,5,6,7,8,9

for i in range(0,10,1):
    print(i)    # output: 0,1,2,3,4,5,6,7,8,9

# if you had function named bacon() inside a module named spam
# how would you call it after importing spam?
# ans:  import spam
#       print(spam.bacon())
