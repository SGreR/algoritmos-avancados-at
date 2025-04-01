from Grafo import  Grafo

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