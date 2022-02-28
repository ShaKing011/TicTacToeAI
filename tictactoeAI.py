#0 = space 
#1 = X = computer
#2 = O = human
import itertools
import random
import math
#X wins = 10
#0 wins = -10
#Draw = -1
#Nothing = 0
def wincheck(board):

#win condition horizontal check 
    for i in range(3):
    
        if board[i].count(1) == 3:

            print("CROSSES WINS")
            return 10
        if board[i].count(2) == 3:

            print("KNOTS WINS")
            return -10
   
#check vertical
    for j in range(3):
        Xcount = 0
        Ocount = 0
        for i in range(3):
            if board[i][j] == 1:
                Xcount += 1
            if board[i][j] == 2:
                Ocount += 1 
        if Ocount == 3:

            print("KNOTS WINS")
            return -10
        if Xcount == 3:

            print("CROSSES WINS")
            return 10

#check lead diagnal
    Xcount = 0
    Ocount = 0
    for i in range(3):
        j = i
        if board[i][j] == 1:
            Xcount += 1
        if board[i][j] == 2:
            Ocount += 1 
    if Ocount == 3:

        print("KNOTS WINS")
        return -10
    if Xcount == 3:

        print("CROSSES WINS")
        return 10
#check back diagnal
    Xcount = 0
    Ocount = 0
    for i in range(3):
        j = 2-i
        if board[i][j] == 1:
            Xcount += 1
        if board[i][j] == 2:
            Ocount += 1 
    if Ocount == 3:

        print("KNOTS WINS")
        return -10
    if Xcount == 3:

        print("CROSSES WINS")
        return 10

    drawCount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                drawCount += 1
    if drawCount == 9:

        print("DRAW")
        return -1
    return 0


def changeplayer(player):
    if player ==1:
        print("O turn")               
        return 2 
        
    elif player ==2:
        print("X turn")  
        return 1       
        
def makeMove(x,y, player):
    if board[x][y] == 0:
        board[x][y] = player  
    else:
        print("illegal move")
        while  (x > 2) or (x <0) or (y > 2) or (y <0): 
            print("Enter Co Ordinates:")
            y, x = input("Enter Co Ordinates:").split(" ")
            x= int(x)
            y = int(y)

     
        
def printboard(board):
    for i in range(3):
        print("\n") 
        for j in range(3):
            if board[i][j] == 0: print("_", end = " ")
            if board[i][j] == 1: print("X", end = " ")
            if board[i][j] == 2: print("O", end = " ") 






#ENGINE
def numEmpty(board):
    emptCount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                emptCount += 1
    return emptCount

def indexOfEmpty(board):
    indexArray = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                indexArray.append([j,i])
    return indexArray


def getmove(board):
    return random.choice([[1,1], [0,0] , [2,2], [2,0] , [0,2]])


def minimax(board, isMax):
    score = wincheck(board)
    if score == 10:
        return score
    elif score == -10:
        return score
    elif score == -1:
        return score
    
    if isMax:
        best = -100
        for i in range(3):
            for j in range(3):
                if board[i][j] ==0:
                    board[i][j] = 1
                    best = max(best, minimax(board, not isMax))
                    board[i][j] =0
                    book[str(board)] = best   
                 
        return best
    else:
        best = 100
        for i in range(3):
            for j in range(3):
                if board[i][j] ==0:
                    board[i][j] = 2
                    best = min(best, minimax(board, not isMax))
                    board[i][j] =   0
                    book[str(board)] = best
        
        return best


    

book = {}
def findBestMove(board) :
    
    bestVal = -100
    bestMove = [-1, -1]

    for i in range(3) :     
        for j in range(3) :
            if (board[i][j] == 0) :
                board[i][j] = 1
                if str(board) in book:
                    moveVal = book[str(board)]
                else:
                    moveVal = minimax(board, 0)
                    book[str(board)] = moveVal
                board[i][j] = 0
    
                if (moveVal >= bestVal) :               
                    bestMove = [i, j]
                    bestVal = moveVal
    return bestMove









 
#GAME SCRIPT
board = [ [0,0,0] , [0,0,0] , [0,0,0] ]
player = 2
while wincheck(board)  == 0:
    printboard(board)

#CHECK FOR LEGIT INPUT
    if player == 2:
        y, x = input("Enter Co Ordinates:").split()
        x= int(x)
        y = int(y)

        while  (x > 2) or (x <0) or (y > 2) or (y <0): 
            y, x = input("Enter Co-Ordinates:").split()
            x= int(x)
            y = int(y)
        makeMove(x,y,player)
        player = changeplayer(player)
        continue
#for engine to play
    else:
        moves = findBestMove(board)
        makeMove(moves[0],moves[1],player)
        player = changeplayer(player)
        continue     
printboard(board)

