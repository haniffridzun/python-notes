while True:
    print('enter your age:')
    age = input()
    if age.isdecimal():     # return True if string consists decimal
        break
    print('please enter a number for your age.')

while True:
    print('select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():  # return True if string consists only num and letter
        break
    print('password can only have letters and numbers.')


# startswith() :: returns True if string value begins with
# 'hello world'.startswith('hello')
# output: True

# endswith() :: returns True if string value ends with
# 'hello world'.endswith('hello')
# output: False

# join() :: join together a list of strings into single string value
# ', '.join(['cats', 'rats', 'bats'])
# output: 'cats, rats, bats'

# split() :: pass a delimiter string to specify a different string to split upon
# 'my2name2is2simon'.split('2')
# output: ['my', 'name', 'is', 'simon']
