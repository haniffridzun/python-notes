import random

messages = ['it is certain',                            # 0
            'it is decidedly so',                       # 1
            'yes definitely',                           # 2
            'reply hazy try again',                     # 3
            'ask again later',                          # 4
            'concentrate and ask again',                # 5
            'my reply is no',                           # 6
            'outlook not so good',                      # 7
            'very doubtful']                            # 8

# print(len(messages))                                  # 9
# print(random.randint(0, len(messages)))               # 0 - 9
print(messages[random.randint(0, len(messages) - 1)])   # 0 - 8

'''
list value is MUTABLE data type: it can have values added, removed, changed

string is IMMUTABLE: it cannot be changed.
proper way to mutate a string is to use slicing and
concatenation to build new string by copying parts of old string.

'''
