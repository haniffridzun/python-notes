name = ''	# 0 / 0.0 / '' are considered False
while not name:
	print('enter your name:')
	name = input()
print('how many guest will you have?')
numOfGuests = int(input())
if numOfGuests:
	print('be sure to have enough room for all your guests.')
print('done')