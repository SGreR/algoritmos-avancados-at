from Grafo import Grafo
from FloydWarshall import floyd_warshall

bairros_floyd_warshall = Grafo()
bairros_floyd_warshall.adicionar_vertice("CD")
bairros_floyd_warshall.adicionar_vertice("A")
bairros_floyd_warshall.adicionar_vertice("B")
bairros_floyd_warshall.adicionar_vertice("C")
bairros_floyd_warshall.adicionar_vertice("D")
bairros_floyd_warshall.adicionar_vertice("E")
bairros_floyd_warshall.adicionar_vertice("F")

bairros_floyd_warshall.adicionar_aresta("A", "B", 5, True)
bairros_floyd_warshall.adicionar_aresta("A", "C", 10, True)
bairros_floyd_warshall.adicionar_aresta("B", "C", 3, True)
bairros_floyd_warshall.adicionar_aresta("B", "D", 8, True)
bairros_floyd_warshall.adicionar_aresta("C", "D", 2, True)
bairros_floyd_warshall.adicionar_aresta("C", "E", 7, True)
bairros_floyd_warshall.adicionar_aresta("D", "E", 4, True)
bairros_floyd_warshall.adicionar_aresta("D", "F", 6, True)
bairros_floyd_warshall.adicionar_aresta("E", "F", 5, True)

bairros_floyd_warshall.mostrar_matriz()

resultado = floyd_warshall(bairros_floyd_warshall.grafo_lista)

for chave in resultado:
    print(chave, resultado[chave])

