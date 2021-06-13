'''
parameters and variables that are assigned in called function
are said to exist in that function's local scope.
variables that are assigned outside functions are said to exist
in the global scope.
local scope is created whenever a function is called. when the
function returns, the local scope is destroyed, and these variables
are forgotten.
'''
def spam():
    eggs = 10 # variable eggs is local variable for function spam()
    print(eggs)

spam()      # output: 10
# print(eggs)
# output: eggs is not defined

'''
code in global scope cannot use any local variables
local scope can access global variables
code in function's local scope cannot use variables in any other local scope
'''
def spamNew():
    eggs = 99
    bacon()     # function is called 
    print(eggs)

def bacon():    # when function returns, local scope is destroyed
    ham = 101
    eggs = 0

spamNew()
# output: 99

'''
global variables can be read from a local scope
'''
def spammer():
    print(eggs)

eggs = 42    # global variable scope
spammer()
print(eggs)
# output: 42
# output: 42
