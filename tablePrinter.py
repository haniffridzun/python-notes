'''
write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
assume that all the inner lists will cotain the same number of strings. for
example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

your printTable() function would print following:

    apples Alice dogs
     oranges    Bob cats
    cherries Carol moose
      banana David goose

hint: your code will first have to find the longest string in each of the
inner lists so that the whole column can be wide enough to fit all the
strings. you can store the max width of each column as a list of integers.
the printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the
number of inner lists in tableData. that way, colWidths[0] can store the
width of the longest string in tableData[0], colWidth[1] can store the
width of longest string in tableData[1], and so on. you can then find the
largest value in the colWidths list to find out what integer width to pass
to the rjust() string method.
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    colWidths = [0] * len(data)         # create new list [0, 0, 0] for tableData
    for y in range(len(data)):          # search for longest string in each list
        for x in data[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)   # put the numbers of characters in new list
    
    for x in range(len(data[0])):
        for y in range(len(data)):
            print(data[y][x].rjust(colWidths[y]), end=' ')
        print()
        x +=1

printTable(tableData)

