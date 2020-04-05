def findffunction(tree,g,h,paths):
    opened = []
    f = []
    for i in range(0,len(tree)):
        if g[i] == 0:
            for j in range(0,len(paths[i])):
                opened.append(paths[i][j])
        x = g[i] + h[i]
        f.append(x)
    return f,opened

def Asearch(f,end,opened,closed,found,paths):
    while not found:
        minIndex = opened[0]
        #find path with smallest f
        for i in range(1,len(opened)):
            if f[opened[i]] < f[minIndex]:
                minIndex = opened[i]
        
        aux = []
        #take out node from opened
        for i in range(0, len(opened)):
            if opened[i] != minIndex:
                aux.append(opened[i])
        opened = aux
        closed.append(minIndex)

        #opens the nodes connected to that one
        for i in range(0, len(paths[minIndex])):
            opened.append(paths[minIndex][i])

        if minIndex == end:
            found = True
    
    return closed

tree = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
g = [20,30,40,50,10,-10,44,48,0,-10,34,44,10,20,30,40]
h = [40,30,20,10,10,-10,10,0,100,-10,20,10,50,40,30,20]
paths =[
[1,4],
[0,2,6],
[1,3,6,8],
[2,6,8],
[0,1,8],
[],
[1,2,3,8,10,11],
[2,3,6,10,11],
[4,12,13],
[],
[6,7,11,13,14,15],
[6,7,10,14,15],
[8,13],
[10,12,14],
[10,11,13,15],
[10,11,14],
]

start = 8
end = 7
found = False

closed = []
closed.append(start)
f, opened = findffunction(tree,g,h,paths)

closed = Asearch(f,end,opened,closed,found,paths)
print(closed)

