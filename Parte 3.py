from Dijkstra import dijkstra, rota_dijkstra
from Grafo import Grafo
from FloydWarshall import floyd_warshall

#Ex6
bairros = Grafo()

bairros.adicionar_vertice("CD")
bairros.adicionar_vertice("A")
bairros.adicionar_vertice("B")
bairros.adicionar_vertice("C")
bairros.adicionar_vertice("D")
bairros.adicionar_vertice("E")
bairros.adicionar_vertice("F")

bairros.adicionar_aresta("CD", "A", 4, True)
bairros.adicionar_aresta("CD", "B", 2, True)
bairros.adicionar_aresta("A", "C", 5, True)
bairros.adicionar_aresta("A", "D", 10, True)
bairros.adicionar_aresta("B", "A", 3, True)
bairros.adicionar_aresta("B", "D", 8, True)
bairros.adicionar_aresta("C", "D", 2, True)
bairros.adicionar_aresta("C", "E", 4, True)
bairros.adicionar_aresta("D", "E", 6, True)
bairros.adicionar_aresta("D", "F", 5, True)
bairros.adicionar_aresta("E", "F", 3, True)

bairros.mostrar()
rota, distancia = rota_dijkstra(bairros.grafo_lista, "CD", "F")
print("Rota:", rota, "Distância:", distancia, "Km")

#Ex7
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
print(floyd_warshall(bairros_floyd_warshall.grafo_lista))

