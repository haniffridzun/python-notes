while True:
    print('who are you?')
    name = input()
    if name != 'joe':
        continue
    # continue statement causes the program execution
    # to jump back to the start of the loop
    print('hello, joe. what is the password? (it is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('access granted!')
