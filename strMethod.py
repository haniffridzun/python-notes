# upper(), lower() methods

spam = 'Hello world!'
print(spam.upper())
# output: 'HELLO WORLD!'
print(spam.lower())
# output: 'hello world!'


print('how are you?')
feeling = input()
if feeling.lower() == 'great':
    print('i feel great too.')
else:
    print('i hope the rest of your day is good.')


# isupper(), islower() methods
'hello'.upper().lower()
# output: 'hello'
'HELLO'.lower().islower()
# output: True


# isalpha() :: returns True if string consists only of letters and is not blank
# isalnum() :: returns True if string consists only letters and number and not blank
# isdecimal() :: returns True if string consists only numeric char and not blank
# isspace() :: returns True if string consists only spaces, tabs, and newlines and not blank
# istitle() :: returns True if string consists only words that begin with uppercase letter
