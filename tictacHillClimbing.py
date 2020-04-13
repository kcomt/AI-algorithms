tictac = [0,0,0,0,0,0,0,0,0]

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

checkForWinner(tictac)