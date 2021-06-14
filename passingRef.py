def eggs(someParameter):
    someParameter.append('hello') # return value is not used to assign new value

spam = [1,2,3]
eggs(spam)      # it modifies the list in place, directly
print(spam)

'''
even though spam and someParameter contain separate references, they both
refer to the same list. this is why append('hello') method call inside the
function affects the list even after the  function call has returned
'''
