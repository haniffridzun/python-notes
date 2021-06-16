#! python3
# passLock - an insecure password locker program

'''
that acc password will be copied to the clipboard so that user
can paste it into password field. this way, user can have long
complicated passwords without having to memorize them.
'''

PASSWORD = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

'''
command line arguments will be stored in variable sys.argv. the first
item in the sys.argv list should always be a string containing program's
filename ('passLock.py'), the second item should be first command line
argument. for this program, this argument is the name of account whose
password you want. since the command line argument is mandatory, you
display a usage message to the user if they forget to add it (that is,
if the sys.argv list has fewer than two values in it).
'''

import sys, pyperclip   # import module to be used

if len(sys.argv) < 2:
    print('usage: python passlock.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

'''
now that account name is stored as sting in variable account, you need
to see whether it exists in password dictionary as a key. if so, you want
to copy the key's value to the clipboard using pyperclip.copy(). note that
you dont actuallly need the account variable; you could just use sys.argv[1]
everywhere account is used in program. but variable named account is much
more readable than something cryptic like sys.argv[1]
'''

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('password for ' + account + ' copied to clipboard')
else:
    print('there is no account named ' + account)
