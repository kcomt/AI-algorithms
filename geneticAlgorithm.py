import random
random.seed()
board = [[" "," "," "," "," "," "," "," "], #0
         [" "," "," "," "," "," "," "," "], #1
         [" "," "," "," "," "," "," "," "], #2
         [" "," "," "," "," "," "," "," "], #3
         [" "," "," "," "," "," "," "," "], #4
         [" "," "," "," "," "," "," "," "], #5
         [" "," "," "," "," "," "," "," "], #6
         [" "," "," "," "," "," "," "," "]] #7
          #0,  1,  2,  3,  4,  5,  6,  7

#Creates a random individual
def createRandomIndividual():
    arr = []
    numbers = [0,1,2,3,4,5,6,7]

    for i in range(0,8):
        aux = random.randrange(0,len(numbers))
        arr.append(numbers[aux])
        numbers.pop(aux)
    return arr

#transform individual to matrix
def transformArrayToMatrix(board, arr):
    auxBoard = []
    for i in board:
        auxBoard.append(i.copy())
    
    for i in range(0,len(arr)):
        auxBoard[arr[i]][i] = "Q"
    
    return auxBoard

#Number of individuals or population
N = 4
def createPopulation(N):
    individuals = []
    for i in range(N):
        individuals.append(createRandomIndividual())
    return individuals

#give a coordinate of a queen, find how many other queen she attacks
def findNumberOfIndividualAttacks(board,coordinate):
    numberOfAtk = 0
    posyFrom = coordinate[0]
    poxFrom = coordinate[1]

    #validate if any queen NorthEast
    iteratory = posyFrom
    iteratorx = poxFrom
    while iteratory >= 0 and iteratorx < 8:
        iteratory -= 1
        iteratorx += 1 
        if board[iteratory][iteratorx] == "Q":
            numberOfAtk += 1
    
    #validate if any queen SouthEast
    iteratory = posyFrom
    iteratorx = poxFrom
    while iteratory < 8 and iteratorx < 8:
        iteratory += 1
        iteratorx += 1 
        if board[iteratory][iteratorx] == "Q":
            numberOfAtk += 1

    #validate if any queen NorthWest
    iteratory = posyFrom
    iteratorx = poxFrom
    while iteratory >= 0 and iteratorx >= 0:
        iteratory -= 1
        iteratorx -= 1 
        if board[iteratory][iteratorx] == "Q":
            numberOfAtk += 1

    #validate if any queen SouthWest
    iteratory = posyFrom
    iteratorx = poxFrom
    while iteratory < 8 and iteratorx >= 0:
        iteratory += 1
        iteratorx -= 1 
        if board[iteratory][iteratorx] == "Q":
            numberOfAtk += 1

    return numberOfAtk
#given a board, it finds number of attacks on board
def findNumberOfAttacksOfBoard(individual):
    coordinates = []
    #find all coordinates of queens [file,column]
    for i in range(0,len(individual)):
        auxCoordinate = []
        auxCoordinate.append(i)
        auxCoordinate.append(individual[i])
        coordinates.append(auxCoordinate)
    
    for i in range(0,len(coordinates)):

population = createPopulation(N)
print(population)
findNumberOfAttacksOfBoard(population[0])
