#Author: Nhan Dao
#Date  : Wed 20/06/18

#Description:

import numbers
import os

gameBoard = [['1','2','3'],
             ['4','5','6'],
             ['7','8','9']]

def printGameBoard(gameBoard):
    board = """
                ? | ? | ?
               ---+---+---
                ? | ? | ?
               ---+---+---
                ? | ? | ?
                           """
    index = 0
    output_board = list(board)
    for i, char in enumerate(output_board):
        if(char == '?'):
            output_board[i] = gameBoard[int(index/3)][int(index%3)]
            index = index + 1

    print(''.join(output_board))

def checkGameCondition(gameBoard,index,symbol):
    hor = True
    ver = True
    dia1 = True
    dia2 = True

    for i in range(0,3):
        if(gameBoard[int(index/3)][i] != symbol):
            hor = False
        if(gameBoard[i][index%3] != symbol):
            ver = False
        if(gameBoard[i][i] != symbol):
            dia1 = False
        if(gameBoard[i][2-i] != symbol):
            dia2 = False

    return hor or ver or dia1 or dia2

def startGame():
    gameFinished = False
    turn = 0
    while(not gameFinished):
        symbol = 'x'
        if(turn%2 == 1):
            symbol = 'o'

        os.system('clear')
        printGameBoard(gameBoard)
        num = 0
        try:
            num = input("Enter 1-9: ")
            num = int(num) - 1
            print(num)
            if(gameBoard[int(num/3)][num%3] != 'x' and gameBoard[int(num/3)][num%3] != 'o'):
                gameBoard[int(num/3)][num%3] = symbol
                gameFinished = checkGameCondition(gameBoard,num,symbol)
                turn = turn + 1

        except (ValueError,IndexError, TypeError):
            pass



    os.system('clear')
    printGameBoard(gameBoard)

startGame()
