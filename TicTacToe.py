import sys

# Define the Board for the Game
Board = {'top-L': '', 'top-M': '', 'top-R': '',
         'mid-L': '', 'mid-M': '', 'mid-R': '',
         'low-L': '', 'low-M': '', 'low-R': ''}

GameBoard = {'top-L': 7, 'top-M': 8, 'top-R': 9,
             'mid-L': 4, 'mid-M': 5, 'mid-R': 6,
             'low-L': 1, 'low-M': 2, 'low-R': 3}

# Print out a board and associate values
def printBoard(board: object) -> object:
    print(board['top-L'].rjust(3, ' ') + '|' + board['top-M'].rjust(3, ' ') + ' |' + board['top-R'])
    print('-- + -- + --')
    print(board['mid-L'].rjust(3, ' ') + '|' + board['mid-M'].rjust(3, ' ') + ' |' + board['mid-R'])
    print('-- + -- + --')
    print(board['low-L'].rjust(3, ' ') + '|' + board['low-M'].rjust(3, ' ') + ' |' + board['low-R'])


# A Function for update the board based on the userInput
def updateBoard(inp, board, user):
    check = board.get(inp, "None")
    if check == "None":
        return
    elif check == symbolInput or check == systemPlaySymbol:
        print("That spot is already taken - Choose another one")
        return
    else:
        board[inp] = user

def winboard():
    return "None"

def calculateWinner(symbol):
    checkList = []
    win =''
    winning_combination = [[7, 8, 9], [4, 6, 5], [1, 2, 3], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for key, values in Board.items():
        if values == symbol:
            checkList.append(GameBoard[key])
    #for i in len(winning_combination)
    for i in range(0, len(winning_combination)):
        if set(checkList) == set(winning_combination[i]):
            win = 'W'
    return win


# Ask for input from User
print("Would you like to Play Tic-Tac-Toe with me?")
userInput = input().lower()
if not userInput:
    print('You typed nothing - restart me')
    sys.exit(0)

while userInput:
    if userInput == 'yes':
        break
    if userInput == 'no':
        print('You typed NO - restart me')
        sys.exit(0)
    print("Say yes or no - not anything else please")
    userInput = input().lower()

print('All right lets play')

print("Choose a symbol for your play --X or O?")
symbolInput = input()
if symbolInput == 'O':
    systemPlaySymbol = 'X'
else:
    systemPlaySymbol = 'O'
print("You are gonna be using " + symbolInput + " for your game" + '\n'
                                                          "I am gonna be using " + systemPlaySymbol + " for my moves")

# noinspection PyGlobalUndefined
win = ''
printBoard(Board)
while not win:
    print("Pick your spot")
    userMove = input()
    while not userMove:
        print("Enter your right spot")
        userMove = input()
    while not userMove in Board.keys():
        print("Pick a valid spot")
        userMove = input()
    updateBoard(userMove, Board, symbolInput)
    printBoard(Board)
    win = calculateWinner(symbolInput)
    if win:
        print("You won " + symbolInput)
        break
    print("Next is my turn")
    comMove = input()
    #ComSpot = winboard()
    updateBoard(comMove, Board, systemPlaySymbol)
    printBoard(Board)
    win = calculateWinner(systemPlaySymbol)
    if win:
        print("You won " + systemPlaySymbol)
        break




