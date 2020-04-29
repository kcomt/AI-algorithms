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
        auxBoard[arr[i]][i] = "R"
    
    return auxBoard

#Number of individuals or population
N = 4
def createPopulation(N):
    individuals = []
    for i in range(N):
        individuals.append(createRandomIndividual())
    return individuals

def findNumberOfIndividualAttacks(arr):

#given a board, it finds number of attacks on board
def findNumberOfAttacksOfBoard(individual):
    #find all coordinates of queens
    
def ideonidadFinder(population):

population = createPopulation(N)
print(population)
