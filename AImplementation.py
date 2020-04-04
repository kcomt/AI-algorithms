def findffunction(tree,g,h):
    opened = []
    f = []
    for i in range(0,len(tree)):
        if g[i] != 0:
            opened.append(i)
        x = g[i] + h[i]
        f.append(x)
    return f,opened

tree = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
g = [20,30,40,50,10,-10,44,48,0,-10,34,44,10,20,30,40]
h = [40,30,20,10,10,-10,10,0,100,-10,20,10,50,40,30,20]
paths =

start = 8
end = 7
found = False

closed = []
closed.append(start)
f, opened = findffunction(tree,g,h)

def Asearch(start,end,open,closed,tree,found):
    if not found:
        minimum = open[0]
        for i in range(1,len(open)):
            if open[i] < minimum:





