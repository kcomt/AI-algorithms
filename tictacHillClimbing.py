#prints board in console
def printBoard(arr):
    columns = []
    line1 = arr[0:3]
    line2 = arr[3:6]
    line3 = arr[6:9]
    columns.append(line1)
    columns.append(line2)
    columns.append(line3)
    for i in range(0, len(columns)):
        print(columns[i])

#checks to see whats the heuristic function (its value)
def checkForWinner(arr, char):
    f = 0
    #check horizontally
    for i in range(0,len(arr),3):
        aux = 0
        if arr[i] == char:
            aux = aux + 1
        if arr[i+1] == char:
            aux = aux + 1   
        if arr[i+2] == char:
            aux = aux + 1 
        if aux > f:
            f = aux

    #check vertically
    for i in range(0,3):
        aux = 0
        if arr[i] == char:
            aux = aux + 1
        if arr[i+3] == char:
            aux = aux + 1   
        if arr[i+6] == char:
            aux = aux + 1 
        if aux > f:
            f = aux
            
    #check diagnolaly
    for i in range(0,3,2):
        if i == 0:
            aux = 0
            if arr[i] == char:
                aux = aux + 1
            if arr[i+4] == char:
                aux = aux + 1   
            if arr[i+8] == char:
                aux = aux + 1 
            if aux > f:
                f = aux
        
        if i == 2:
            aux = 0
            if arr[i] == char:
                aux = aux + 1
            if arr[i+2] == char:
                aux = aux + 1   
            if arr[i+4] == char:
                aux = aux + 1 
            if aux > f:
                f = aux
    
    return f

#checks for possible win lines
def checkPossibleWinLines(arr,char):
    number = 0

    #check horizontal win lines
    for i in range(0,len(arr),3):
        aux = 0
        if arr[i] != char and arr[i+1] != char and arr[i+2] != char:
            number += 1
    
    #check vertical win lines
    for i in range(0,3):
        if arr[i] != char and arr[i+3] != char and arr[i+6] != char:
            number += 1


    #check diagnolal win lines
    for i in range(0,3,2):
        if i == 0:
            if arr[i] != char and arr[i+4] != char and arr[i+8] != char:
                number += 1
        
        if i == 2:
            if arr[i] != char and arr[i+2] != char and arr[i+4] != char:
                number += 1
    
    return number

def findF(arr,char):
    if char == "x":
        charAI = "o"
    else:
        charAI = "x"
    
    posPlayer = checkPossibleWinLines(arr,charAI)
    posAI = checkPossibleWinLines(arr,char)

    return posPlayer-posAI

#find positions left
def findPositionsLeft(arr):
    positionsLeft = []
    for i in range(0, len(arr)):
        if arr[i] == " ":
            positionsLeft.append(i)
    return positionsLeft

def play(arr,char,winner):
    while not winner:
        positionsLeft = findPositionsLeft(arr)
        # if player picks x, he goes first, else computer goes first
        if char == "x":
            #player plays
            print("\nPositions that are left: ")
            print(positionsLeft)
            posi = input('\nWhere do you want to put?: ')
            posi = int(posi)
            arr[posi] = "x"
            printBoard(arr)

            if checkForWinner(arr,"x") >= 3:
                winner = True
                print("\nHas ganado la partida!")

            else:
                #player hasnt won so computer plays
                positionsLeft = findPositionsLeft(arr)
                possibleStates = []
                for i in range(0, len(positionsLeft)):
                    aux = []
                    aux = arr.copy()
                    aux[positionsLeft[i]] = "o"
                    possibleStates.append(aux)
            
                #Array of positions that would be placed and their respective f
                ranking = []
                for i in range(0, len(positionsLeft)):
                    aux = []
                    aux.append(positionsLeft[i])
                    aux.append(findF(possibleStates[i],"x"))
                    ranking.append(aux)

                #find most f and make it the current state
                mini = ranking[0][1]
                arr = possibleStates[0]
            
                for i in range(0, len(ranking)):
                    if mini > ranking[i][1]:
                        mini = ranking[i][1]
                        arr = possibleStates[i]
                
                #Show the player that the AI has played
                print("\nLa computadora ha jugado: ")
                printBoard(arr)

                if checkForWinner(arr,"o") >= 3:
                    winner = True
                    print("La computadora ha ganado")
            
        else:
            positionsLeft = findPositionsLeft(arr)
            possibleStates = []
            for i in range(0, len(positionsLeft)):
                aux = []
                aux = arr.copy()
                aux[positionsLeft[i]] = "x"
                possibleStates.append(aux)
            
            #Array of positions that would be placed and their respective f
            ranking = []
            for i in range(0, len(positionsLeft)):
                aux = []
                aux.append(positionsLeft[i])
                aux.append(findF(possibleStates[i],"o"))
                ranking.append(aux)

            #find most f and make it the current state
            mini = ranking[0][1]
            arr = possibleStates[0]
            
            for i in range(0, len(ranking)):
                if mini > ranking[i][1]:
                    mini = ranking[i][1]
                    arr = possibleStates[i]
                
            #Show the player that the AI has played
            print("\nLa computadora ha jugado: ")
            printBoard(arr)

            if checkForWinner(arr,"x") >= 3:
                winner = True
                print("La computadora ha ganado")
            else:
                #computer hasnt won so player playss
                print("\nPositions that are left: ")
                print(positionsLeft)
                posi = input('\nWhere do you want to put?: ')
                posi = int(posi)
                arr[posi] = "o"
                printBoard(arr)

                if checkForWinner(arr,"o") >= 3:
                    winner = True
                    print("\nHas ganado la partida!")
        
board = [0,1,2,3,4,5,6,7,8]
tictac = [" "," "," "," "," "," "," "," "," "]
print("This is the board, and its respective positions: ")
printBoard(board)
char = input('\nWhat do you want to play as "x" or "o": ')
play(tictac,char,False)

