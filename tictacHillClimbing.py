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

#checks if there is a winner to leave loop
def checkForWinner(arr):
    #check horizontally
    for i in range(0,len(arr),3):
        if arr[i] == arr[i+1] and arr[i] == arr[i+2] and arr[i+1] == arr[i+2]:
            return True

    #check vertically
    for i in range(0,3):
        if arr[i] == arr[i+3] and arr[i] == arr[i+6] and arr[i+3] == arr[i+6]:
            return True
            
    #check diagnolaly
    for i in range(0,3,2):
        if i == 0:
            if arr[i] == arr[i+4] and arr[i] == arr[i+8] and arr[i+4] == arr[i+8]:
                return True
        
        if i == 2:
            if arr[i] == arr[i+2] and arr[i] == arr[i+4] and arr[i+2] == arr[i+4]:
                return True

#checks to see whats the heuristic function (its worth)
def findf(arr, char):
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
            if arr[i+4] == char:
                aux = aux + 1   
            if arr[i+6] == char:
                aux = aux + 1 
            if aux > f:
                f = aux
    
    return f

def play(arr,char):
    positionsLeft = []
    #find positions left
    for i in range(0, len(arr)):
        if tictac[i] == " ":
            positionsLeft.append(i)

    if char == "x":
        #player plays

        print("\nPositions that are left: ")
        print(positionsLeft)
        posi = input('\nWhere do you want to put?: ')
        posi = int(posi)
        arr[posi] = "x"
        printBoard(arr)

        if findf(arr,"x") > 3:
            print("\nHas ganado la partida!")
        else:
            #player hasnt won so computer plays
            
    else:
        print("es igual a o")


board = [0,1,2,3,4,5,6,7,8]
tictac = [" "," "," "," "," "," "," "," "," "]
print("This is the board, and its respective positions: ")
printBoard(board)
char = input('\nWhat do you want to play as "x" or "o": ')
play(tictac,char)

