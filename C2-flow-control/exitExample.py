import sys # import system module

while True:
    print('type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
        # this program has an infinite loop with no break statement
        # the only way this program will end is if the user enters exit
        # causing sys.exit() to be called
        # when response is equal to exit, program ends.
    print('you typed ' + response + '.')
