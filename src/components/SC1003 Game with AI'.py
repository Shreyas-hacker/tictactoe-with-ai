# tic tac toe

# board with a bunch of blank spaces
board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

#check if space in board is empty
def spaceisFree(pos):
    return board[pos] == " "

#printing the board
def printBoard(board):
    print('    |    |')
    print(' '  +  board[1] + ' | '+board[2]+' | '+board[3])
    print('    |    |')
    print('-----------')
    print('    |    |')
    print(' '  +  board[4] + ' | '+board[5]+' | '+board[6])
    print('    |    |')
    print('-----------')
    print('    |    |')
    print(' '  +  board[7] + ' | '+board[8]+' | '+board[9])
    print('    |    |')

#determin the winner
def isWinner(bo,le):
    return (bo[7] == le and bo[8]==le and bo[9]==le) or (bo[4] == le and bo[5] == le and bo[6] ==le) or (bo[1]==le and bo[2] == le and bo[3]==le) or (bo[1] == le and bo[4]==le and bo[7]==le) or (bo[2] == le and bo[5]==le and bo[8]==le) or (bo[3] == le and bo[6]==le and bo[9]==le) or (bo[1] == le and bo[5]==le and bo[9]==le) or (bo[3] == le and bo[5]==le and bo[7]==le)

def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9)")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number between 1 to 9!')
        except:
            print('Please type a number!')

def compMove():
    pass

def selectRandom(board):
    pass

#checking if board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return True
    else:
        return False

def game():
    print('Welcome to Tic Tac Toe!')
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMove()
            printBoard()
        else:
            print('Sorry, O\'s won this time')
            break

        if not(isWinner(board,'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', board)
                print('Computer placed an \'O\' in position', move,':')
                printBoard()
        else:
            print('Congrats, X\'s won this time')
            break
    if isBoardFull(board):
        print('Tie Game')

if __name__=="__main__":
    game()