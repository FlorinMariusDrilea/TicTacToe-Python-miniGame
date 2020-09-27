import random

board = [' ' for x in range(10)]

def insertLetter(letter, position):
    board[position] = letter

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)

def freeSpace(position):
    return board[position] == ' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('   |   |   ')
    print('------------')

def fullBoardCheck(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def winner(board,l):
    return ((board[1] == l and board[2] == l and board[3] == l) or (board[4] == l and board[5] == l and board[6] ==l) or (board[7] == l and board[8] == l and board[9] == l) or(board[1] == l and board[4] == l and board[7] == l) or(board[2] == l and board[5] == l and board[8] == l) or(board[3] == l and board[6] == l and board[9] == l) or(board[1] == l and board[5] == l and board[9] == l) or(board[3] == l and board[5] == l and board[7] == l))

def playerMovement():
    run = True
    while run:
        move = input("Please select a position to enter the X  between 1 and 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freeSpace(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("This space is unavailable!")
            else:
                print("Type a number between 1 and 9")
        except:
            print("Please type a number!")

def movementAI():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x!= 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    cornersOpen = []

    for i in possibleMoves:
        if i in [1 , 3, 7, 9]:
            cornersOpen.append[i]
        
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgeOpen = []

    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgeOpen.append[i]
    
    if len(edgeOpen) > 0:
        move = selectRandom(edgeOpen)
        return move
    
def main():
    print("Welcome!")
    printBoard(board)

    while not(fullBoardCheck(board)):
        if not(winner(board , 'O')):
            playerMovement()
            printBoard(board)
        else:
            print("You lost!")
            break

        if not(winner(board , 'X')):
            move = movementAI()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('Computer placed an o on position' , move , ':')
                printBoard(board)
        else:
            print("Winner!")
            break

    if fullBoardCheck(board):
        print("Tie game")