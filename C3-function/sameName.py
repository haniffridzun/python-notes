def spam():
    eggs = 'spam local'
    print(eggs)     # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)     # prints 'bacon local'
    spam()          # call spam() function, return local variable and destroyed
    print(eggs)     # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)         # prints 'global'

'''
4 rules to tell whether variable is in local scope or global scope
- if variable is being used in global scope, then it is always global var
- if there is global keyword for that variable, it is a global var
- otherwise, if the variable is used in an assignment statement in function,
  it is local variable
- but if the variable is not used in an assignment statement, it is a global var
'''
def spammer():
    global eggs     # global keyword set variable to global scope
    eggs = 'spam'

eggs = 'global'
spammer()
print(eggs)
# output: spam

def baconNew():
    eggs = 'bacon'  # this is local scope

def ham():
    print(eggs)     # this use global scope

eggs = 42           # this is global
ham()               # refer to eggs = 42 global var
spammer()           # call global var in spammer()
print(eggs)         # output: spam

def spams():
    print(eggs)     # if you try to use local variable in a function before
                    # you assign a value to it, python will give error
    eggs = 'spam local' 

eggs = 'global'
spams()
# output: error
'''
happens because python sees that there is an assignment statement for
eggs in spams() function and therefore considers eggs to be local.
python will not fall back to using global eggs variable
'''
