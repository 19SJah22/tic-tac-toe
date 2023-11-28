# Begin
# creating a board to start from range(0,10) to get a 3x3 grid
board = [' ' for x in range(10)]

# Making a function to select where player wants to play


def insertmove(letter, position):
    board[position] = letter

# looking to see if space is free


def freespace(posistion):
    return board[posistion] == ' '


def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

# Creating a function to stop loop if the board is full


def fullboard(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# creating a def to see if there is a winnner


def checkwinner(theboard, l):
    return ((theboard[1] == l and theboard[2] == l and theboard[3] == l) or
            (theboard[4] == l and theboard[5] == l and theboard[6] == l) or
            (theboard[7] == l and theboard[8] == l and theboard[9] == l) or
            (theboard[1] == l and theboard[4] == l and theboard[7] == l) or
            (theboard[2] == l and theboard[5] == l and theboard[8] == l) or
            (theboard[3] == l and theboard[6] == l and theboard[9] == l) or
            (theboard[1] == l and theboard[5] == l and theboard[9] == l) or
            (theboard[3] == l and theboard[5] == l and theboard[7] == l))

# creating function for player moves


def playerMove():
    run = True
    while run:
        move = input("please select a position to enter the X between 1 to 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freespace(move):
                    run = False
                    insertmove('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('please type a number between 1 and 9')

        except:
            print('Please type a number')

# Creating a computer


def computerMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if checkwinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# The function that executes the hole co


def main():
    print("Welcome to the game!")
    printBoard(board)

    while not(fullboard(board)):
        if not(checkwinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("sorry you loose!")
            break

        if not(checkwinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertmove('O', move)
                print('computer placed an o on position', move, ':')
                printBoard(board)
        else:
            print("you win!")
            break

    if fullboard(board):
        print("Tie game")


while True:
    # ask the user if they wants to play again
    question = input("Do you want to play again? (y/n)")
    if question.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
