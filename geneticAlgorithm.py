import random
random.seed()
board = [["00","00","00","00","00","00","00","00"], #0
         ["00","00","00","00","00","00","00","00"], #1
         ["00","00","00","00","00","00","00","00"], #2
         ["00","00","00","00","00","00","00","00"], #3
         ["00","00","00","00","00","00","00","00"], #4
         ["00","00","00","00","00","00","00","00"], #5
         ["00","00","00","00","00","00","00","00"], #6
         ["00","00","00","00","00","00","00","00"]] #7
          #0,     1,   2,   3,    4,  5,    6,  7

#Creates a random individual
def createRandomIndividual():
    arr = []
    numbers = [0,1,2,3,4,6,7,8]

    for i in range(0,8):
        aux = random.randrange(0,len(numbers))
        arr.append(numbers[aux])
        numbers.pop(aux)
    return arr

#transform individual to matrix

