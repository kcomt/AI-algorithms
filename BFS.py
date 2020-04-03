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

def A(start,paths,h,g,found,foundPath,weightAcum):
    foundPath.append(start)
    if not found:
        possible = paths[start]
        start,weightAcum = succesorA(start,possible,h,g,weightAcum)
        if h[start] == 0:
            found = True
            foundPath.append(start)
            return foundPath, weightAcum
        else:
            return A(start,paths,h,g,found,foundPath,weightAcum)

def succesorA(start,possible,h,g,weightAcum):
    nextNode = possible[0]
    posOfNodeInG = -100

    for j in range(0,len(g[start])):
        if nextNode == g[start][j][0]:
            posOfNodeInG = j

    minimum = h[nextNode] + g[start][posOfNodeInG][1] + weightAcum

    for i in range(0,len(possible)):
        for j in range(0,len(g[start])):
            if possible[i] == g[start][j][0]:
                posOfNodeInG = j

        if h[possible[i]] + g[start][posOfNodeInG][1] + weightAcum < minimum:
            nextNode = possible[i]
            minimum = h[i] + g[start][posOfNodeInG][1] + weightAcum
            weightAcum = weightAcum + g[start][posOfNodeInG][1]
    
    return nextNode, weightAcum

tree = [0,1,2,3,4,5]
paths=[[1,2],[4],[3,4],[4,5],[4]]
found = False
foundPath = []

#Heuristic of distance from any node to node 5
h = [10,8,7,3,0,2]

#[NODE, WEIGHT]
g =[
[[1,4],[2,4]],
[[4,6],[3,3]],
[[3,4]],
[[4,1],[5,3]],
[[5,4]]
]

weightAcum = 0

print(A(0,paths,h,g,found,foundPath,weightAcum))