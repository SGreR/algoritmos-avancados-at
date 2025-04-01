from Grafo import  Grafo

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



