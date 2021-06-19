# rjust()   :: justify to right
# ljust()   :: justify to left
# center()  :: centers the text

# 'hello'.rjust(10)
# output: '          hello'

# 'hello'.rjust(5, '-')
# output: '-----hello'

# 'hello'.ljust(5, 'x')
# output: 'helloxxxxx'

# 'hello'.center(5, '=')
# output: '=====hello====='


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('picnic items'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') +  str(v).rjust(rightWidth))

# dictionary for picnic items
picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies': 800}

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)


# strip()   :: remove whitespace (space, tab, newline) from both side of string
# rstrip()  :: remove whitespace from right side of string
# lstrip()  :: remove whitespace from left side of string
spam = '    hello world    '
spam.strip()    # output: 'hello world'
spam.rstrip()   # output: '    hello world'
spam.lstrip()   # output: 'hello world    '

# specify character to strip, order does not matter
spammer = 'spamspambaconspameggsspamspam'
spammer.strip('amps')
# output: 'baconspamegg'


# copying and pasting strings with pyperclip module
# send text to and receive text from computer's clipboard
# >>> import pyperclop
# >>> pyperclip.copy('hello world')
# >>> pyperclip.paste()
# 'hello world'
