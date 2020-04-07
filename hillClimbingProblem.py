state = [2,4,6,7,1,3,8,5,"*"]

finalState = [1,2,3,8,"*",4,7,6,5]

def moveRandomly(state):
    #find position of *
    for i in range(0,len(state)):
        if state[i] == "*":
            index  = i
    #move up
    if index != 0 or index != 1 or index !=2:
        newIndex = index - 3
        aux = state[0:newIndex-1]
        aux.append(state[index])
        aux2 = state[newIndex:len(state)-1]
        state = aux + aux2
   #move down
    if index != 6 or index != 7 or index !=8:
        newIndex = index + 3
        aux = state[0:newIndex-1]
        aux.append(state[index])
        aux2 = state[newIndex:len(state)-1]
        state = aux + aux2
    #move left
    if index != 0 or index != 3 or index !=6:
        newIndex = index - 2
        aux = state[0:newIndex-1]
        aux.append(state[index])
        aux2 = state[newIndex:len(state)-1]
        state = aux + aux2
    #move right
    if index != 2 or index != 5 or index !=8:
        newIndex = index + 2
        aux = state[0:newIndex-1]
        aux.append(state[index])
        aux2 = state[newIndex:len(state)-1]
        state = aux + aux2

    return state

def hillClimbing(state,finalState):
