# Q1: what is []?
# ans: empty list

# Q2: how to assign value 'hello' as third value in a list stored in a var named
#       spam? (assume spam contains [2,4,6,8,10])
# ans: spam.insert(2, 'hello')

# next 3 questions use spam = ['a', 'b', 'c', 'd']

# Q3: what does spam[int(int('3'*2) / 11)] evaluate to?
# ans: 'd'

# Q4: what does spam[-1] evaluate to?
# ans: 'd'

# Q5: what does spam[:2] evaluate to?
# ans: ['a, 'b']

# next 3 questions use bacon = [3.14, 'cat', 11, 'cat', True]

# Q6: what does bacon.index('cat') evaluate to?
# ans: 1

# Q7: what does bacon.append(99) make the list value in bacon look like?
# ans: [3.14, 'cat', 11, 'cat', True, 99]

# Q8: what does bacon.remove('cat') make the list look like?
# ans: [3.14, 11, 'cat', True, 99]

# Q9: what are the operators for list concatenation and list replication
# ans: list concatenation (+)           list replication (*)

# Q10: difference between append() and insert() list methods?
# ans: append() - add value at the end of list
# ans: insert() - add value at specific index in the list

# Q11: what are two ways to remove values from list?
# ans: del keyword - use index as parameter
# ans: remove() method - use list value as parameter

# Q12: what is the difference between lists and tuples?
# ans: list is mutable and tuples is immutable

# Q13: how do you type tuple value that has just integer value 42 in it?
# ans: (42,)

# Q14: how to get tuple form of a list value? how to get list form of tuple value?
# ans: tuple(list)
# ans: list(tuple)

# Q15: variables that 'contain' list values dont actually contain lists directly.
#       what do they contain instead?
# ans: reference to list values
