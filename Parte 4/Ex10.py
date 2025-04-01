from Grafo import Grafo
from Prim import prim

rede_internet = Grafo()
rede_internet.adicionar_vertice("Cidade_A")
rede_internet.adicionar_vertice("Cidade_B")
rede_internet.adicionar_vertice("Cidade_C")
rede_internet.adicionar_vertice("Cidade_D")
rede_internet.adicionar_vertice("Cidade_E")
rede_internet.adicionar_vertice("Cidade_F")
rede_internet.adicionar_vertice("Cidade_G")

rede_internet.adicionar_aresta("Cidade_A", "Cidade_B", 5, True)
rede_internet.adicionar_aresta("Cidade_A", "Cidade_C", 10, True)
rede_internet.adicionar_aresta("Cidade_B", "Cidade_C", 3, True)
rede_internet.adicionar_aresta("Cidade_B", "Cidade_D", 8, True)
rede_internet.adicionar_aresta("Cidade_C", "Cidade_D", 2, True)
rede_internet.adicionar_aresta("Cidade_C", "Cidade_E", 7, True)
rede_internet.adicionar_aresta("Cidade_D", "Cidade_E", 4, True)
rede_internet.adicionar_aresta("Cidade_D", "Cidade_F", 6, True)
rede_internet.adicionar_aresta("Cidade_E", "Cidade_F", 5, True)
rede_internet.adicionar_aresta("Cidade_F", "Cidade_G", 2, True)
rede_internet.adicionar_aresta("Cidade_G", "Cidade_A", 9, True)

mst, custo_total = prim(rede_internet.grafo_lista, "Cidade_A")

print("Árvore Geradora Mínima (MST) para rede de internet:")
for vertice, custo in mst:
    print(f"Vértice: {vertice}, Custo: {custo}")
print(f"Custo total da MST: {custo_total}")