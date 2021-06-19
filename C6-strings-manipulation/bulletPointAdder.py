#! python3
# bulletPointAdder.py - adds wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

# TODO: separate lines and add starts
lines = text.split('\n')
for i in range(len(lines)):     # loop trough all indexes in 'lines' list
    lines[i] = '* ' + lines[i]  # add start to each string in 'lines' list
text = '\n'.join(lines)
pyperclip.copy(text)
