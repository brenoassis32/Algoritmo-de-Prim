# Algoritmo-de-Prim

## Importando a classe Grafo
~~~python
from class_grafo import *
~~~
Lembre-se que o arquivo class_grafo.py deve estar na mesma pasta do arquivo prim.py

## Passando a quantidade de vértices igual a 4
~~~python
g=Grafo(4)
~~~

## Adicionando arestas seguindo o formato: .addAresta(vértice1, vértice2, peso da aresta)
~~~python
g.addAresta(1, 2, 1)
g.addAresta(1, 4, 2)
g.addAresta(2, 3, 3)
g.addAresta(2, 4, 4)
g.addAresta(3, 4, 5)
~~~

## Executando o algortimo de PRIM
~~~python
g.prim()
~~~

## Obtendo o comprimento da árvore de peso mínimo
~~~python
print(g.retornaValorCusto())
~~~
Resultado igual a 6 no exemplo demonstrado.

## Obtendo a árvore geradora de peso mínimo
~~~python
g.retornaValorRota()
~~~
Resultado de ST = {(1,2);(1,4);(2,3)} no exemplo demonstrado.


## Referências
ARENALES, M. et al., Pesquisa Operacional para Cursos de Engenharia., Rio de Janeiro: Elsevier, 2007.

HILLIER, F.S., LIEBERMAN, G.J. Introduction to Operations Research., MacGraw-Hill, 2001.

TAHA, H.A., Pesquisa Operacional, 8. ed. Pearson Prentice Hall, 2008.

WINSTON, W. Operations Reseach, Applications and Algorithms. Duxbury Press, 2003.

