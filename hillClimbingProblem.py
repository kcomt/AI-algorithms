state = [2,4,6,7,1,3,8,5,"*"]

finalState = [1,2,3,8,"*",4,7,6,5]

def move(state):
    #find position of *
    for i in range(0,len(state)):
        if state[i] == "*":
            index  = i

    #move up
    if index != 0 and index != 1 and index !=2:
        newIndex = index - 3
        aux = state[0:newIndex]
        aux.append(state[index])
        aux2 = state[newIndex:len(state)-1]
        stateUp = aux + aux2
    else:
        stateUp = None

    #move down
    if index != 6 and index != 7 and index !=8:
        newIndex = index + 3
        aux = state[0:newIndex]
        aux.append(state[index])
        aux2 = state[newIndex:len(state)-1]
        stateDown = aux + aux2
    else:
        stateDown = None

    #move left
    if index != 0 and index != 3 and index !=6:
        newIndex = index - 1
        aux = state[0:newIndex]
        aux.append(state[index])
        aux2 = state[newIndex:len(state)-1]
        stateLeft = aux + aux2
    else:
        stateLeft = None

    #move right
    if index != 2 and index != 5 and index !=8:
        newIndex = index + 1
        aux = state[0:newIndex]
        aux.append(state[index])
        aux2 = state[newIndex:len(state)-1]
        stateRight = aux + aux2
    else:
        stateRight = None

    return stateUp,stateDown,stateLeft,stateRight


def findHOfState(state,finalState):
     cont = len(finalState)
     for i in range(0,len(finalState)):
        if state[i] == finalState[i]:
            cont = cont - 1
     return cont
     

def hillClimbing(currentState,finalState):
    hasGoneDown = False
    lastMove = "None"
    while not hasGoneDown:
        f = []
        states = []
        #try up,down,left,right
        stateUp,stateDown,stateLeft,stateRight = move(currentState)
        states.append(stateUp)
        states.append(stateDown)
        states.append(stateLeft)
        states.append(stateRight)
        
        for i in range(0, len(states)):
            if states[i] != None:
                f.append(findHOfState(states[i],finalState))
            else:
                 f.append(10000)

        #find least f and compare to f current state
        posNextState = states[0]
        minF = f[0]
        for i in range(0, len(f)):
            if minF > f[i]:
                minF = f[i]
                posNextState = states[i]

        if minF < findHOfState(currentState,finalState):
            currentState = posNextState
        else:
            hasGoneDown = True

    return currentState

print(hillClimbing(state,finalState))
