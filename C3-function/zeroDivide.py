'''
getting error, or exception, in python program means the entire program will crash.
you dont want this to happen in real world programs. instead, you want program
to detect errors, handle them, then continue to run.
'''
def spam(divideBy):
    return 42 / divideBy

# print(spam(2))
# print(spam(12))
# print(spam(0))  # error
# print(spam(1))  # program stop running
'''
errors can be handled with try and except statement. the code that could have
error is put in try clause. the program execution moves to the start of following
except clause if an error happens.
'''
def spammer(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('error: invalid argument')

print(spammer(2))
print(spammer(12))
print(spammer(0))  # error happen, put into exception
print(spammer(1))  # program continue running
