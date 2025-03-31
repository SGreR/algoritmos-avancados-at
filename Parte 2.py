from Grafo import  Grafo

#Ex 4
cidade = Grafo()
cidade.adicionar_vertice("A")
cidade.adicionar_vertice("B")
cidade.adicionar_vertice("C")
cidade.adicionar_vertice("D")
cidade.adicionar_vertice("E")
cidade.adicionar_vertice("F")

cidade.adicionar_aresta("A", "B", 4)
cidade.adicionar_aresta("A", "C", 2)
cidade.adicionar_aresta("B", "D", 5)
cidade.adicionar_aresta("C", "D", 8)
cidade.adicionar_aresta("C", "E", 3)
cidade.adicionar_aresta("D", "F", 6)
cidade.adicionar_aresta("E", "F", 1)

cidade.mostrar()

#Ex 5
linhas_metro = Grafo()
linhas_metro.adicionar_vertice("A")
linhas_metro.adicionar_vertice("B")
linhas_metro.adicionar_vertice("C")
linhas_metro.adicionar_vertice("D")
linhas_metro.adicionar_vertice("E")
linhas_metro.adicionar_vertice("F")

linhas_metro.adicionar_aresta("A", "B")
linhas_metro.adicionar_aresta("A", "C")
linhas_metro.adicionar_aresta("B", "D")
linhas_metro.adicionar_aresta("B", "E")
linhas_metro.adicionar_aresta("C", "F")
linhas_metro.adicionar_aresta("D", "E")
linhas_metro.adicionar_aresta("E", "F")

linhas_metro.mostrar_lista()

linhas_metro.dfs("A")
linhas_metro.bfs("A")



