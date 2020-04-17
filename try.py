class probar:
    def __init__(self):
        self.arr = [1,2,3,[4,2]]

proba = probar()

aux = proba.arr.copy()
aux[3][0] = "p"
print(proba.arr)