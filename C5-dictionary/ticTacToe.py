# dictionary for board positions
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

# define the board position
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-' )
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-' )
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

turn = 'X'
for i in range(9):          # 9 moves each game
    printBoard(theBoard)    # print current board position
    print('turn for ' + turn + '. choose a number to move?')
    move = input()          # get user move (1 - 9)
    theBoard[move] = turn   # update move for (X/O)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)        # print the board for 9th move
