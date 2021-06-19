print('my name is')
for i in range(5): # i start with 0
    print('jimmy five times (' + str(i) + ')') # concatenate int to string
'''
output:
my name is
jimmy five times (0)
jimmy five times (1)
jimmy five times (2)
jimmy five times (3)
jimmy five times (4)
'''

total = 0
for num in range(101):
    total = total + num
print(total)
'''
output:
5050
'''

# equivalent while loop
print('my name is')
i = 0
while i < 5:
    print('jimmy five times (' + str(i) + ')')
    i = i + 1
'''
output:
my name is
jimmy five times (0)
jimmy five times (1)
jimmy five times (2)
jimmy five times (3)
jimmy five times (4)
'''
