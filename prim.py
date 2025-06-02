from class_grafo import *


g6=Grafo(4)

g6.addAresta(1, 2, 1)
g6.addAresta(1, 4, 2)
g6.addAresta(2, 3, 3)
g6.addAresta(2, 4, 4)
g6.addAresta(3, 4, 5)

g6.prim()
print(g6.retornaValorCusto())
g6.retornaValorRota()
