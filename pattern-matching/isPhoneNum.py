def isPhoneNum(text):
    if len(text) != 12:             # check string if contain 12 characters
        return False
    for i in range(0, 3):
        if not text[i].isdecimal(): # check 1st - 3rd strings are numeric char
            return False
    if text[3] != '-':              # check 4th string is hyphen
        return False
    for i in range(4, 7):           # check 5th - 7th strings are numeric char
        if not text[i].isdecimal():
            return False
    if text[7] != '-':              # check 8th string is hyphen
        return False
    for i in range(8, 12):          # check 9th - 12th strings are numeric char
        if not text[i].isdecimal():
            return False
    return True

# print('415-555-4242 is a phone number:')
# print(isPhoneNum('415-555-4242'))
# print('moshi moshi is a phone number:')
# print(isPhoneNum('moshi moshi'))

message = 'call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):   # loop through 1st - last char in string
    chunk = message[i:i+12]     # get the char to next 12 chars in string
    if isPhoneNum(chunk):       # check the chars is phone number
        print('phone number found: ' + chunk)
print('done')
