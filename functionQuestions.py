# Q1: what statement creates a function
# ans: def funName:

# Q2: what happens to var in local scope when function call returns?
# ans: variable is destroyed and forgotten

# Q3: how to force a var in function to refer to global var?
# ans: use global keyword. example, global varName

# Q4: if you had a function named bacon() in module named spam, how would you call it after importing spam?
# ans: spam.bacon()

# Q5: what goes in the try clause? what goes in the except clause?
# ans: try: all expression that potentially have an error
#      except: code to handle what happens when this error occurs

'''
write function named collatz() that has one parameter named number.
if number is even, then collatz() should print number // 2 and return this value.
if number is odd, then collatz() should print and return 3 * number  + 1.
then write a program that lets user type in an integer and
that keeps calling collatz() on that number until the function returns the value 1.

hint: an integer number is even if number % 2 == 0. and it's odd if number % 2 == 1

output could look something like this
enter number:
3
10
5
16
8
4
2
1
'''
def collatz():
    while True:
        print('enter a positive integer')
        try:
            number = int(input())   # concatenate user input into int
            if number == 0:         # program ends when user enter 0
                break
            while number != 1:
                if number % 2 == 0:
                    print(number // 2)
                    number = number // 2
                elif number % 2 == 1:
                    print(3 * number + 1)
                    number = 3 * number + 1
        except ValueError:
            print('error: input is not positive integer')


collatz()

