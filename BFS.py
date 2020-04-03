
tree = [0,1,2,3,4,5]
paths=[[1,2],[4],[3,4],[4,5],[4]]
#Heuristic of distance from any node to node 5
h = [10,6,7,3,0,2]
found = False
foundPath = []

def bestFirstSearch(start,paths,h,found,foundPath):
    foundPath.append(start)
    if not found:
        possible = paths[start]
        start = succesor(possible,h)
        if h[start] == 0:
            found = True
            foundPath.append(start)
            return foundPath
        else:
            return bestFirstSearch(start,paths,h,found,foundPath)

#find best next node
def succesor(possible,h):
    nextNode = possible[0]
    minimum = h[possible[0]]
    for i in range(0,len(possible)):
        if h[possible[i]] < minimum:
            nextNode = possible[i]
            minimum = h[i] 
    return nextNode

print(bestFirstSearch(0,paths,h,found,foundPath))