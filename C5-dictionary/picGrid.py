'''
say you have list of lists where each value in the inner lists
is a one-character string, like this:

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

you can think of grid[x][y] as being the character at the x and y coordinates
of a picture drawn with text characters. the (0,0) origin will be in the
upper-left corner, the x coordinates increase going right, and the y coordinates
increase going down.
copy previous grid value, and write code that uses it to print the image (love)
..00.00..

.0000000.

.0000000.

..00000..

...000...

....0....
hint: you will need to use a loop in a loop in order to print grid[0][0], then
grid[1][0], then grid[2][0], and so on, up to grid[8][0]. this will finish
the first row, so then print a newline. then your program should print grid[0][1],
then grid[1][1], then grid[2][1], and so on. the last thing your program will
print is grid[8][5]. remember to pass the end keyword to print() if you dont
want a newline printed automatically after each print() call.
'''
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(grid[0][0], end='')     output: .
# print(grid[1][0], end='')     output: .
# print(grid[2][0], end='')     output: 0
for y in range(6):
    print('\n')
    for x in range(len(grid)):
        print(grid[x][y], end='')
