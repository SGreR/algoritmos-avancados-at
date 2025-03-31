#Ex 10
from Grafo import Grafo
from KnightsTour import Cavalo, CavaloHeuristica
from Prim import prim
from CaixeiroViajante import held_karp, vizinho_mais_proximo, algoritmo_genetico
import time

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

#Ex11
tamanhos = [5, 8, 10]

print("Problema do cavalo:")
for tamanho in tamanhos:
    start = time.perf_counter()
    cavalo_heuristica = CavaloHeuristica(tamanho)
    cavalo_heuristica.tabuleiro[0][0] = 0
    cavalo_heuristica.resolver(0, 0, 1)
    end = time.perf_counter()
    print(f"Tempo de execução da heurística de Warnsdorff: {end - start:.6f} segundos")

for tamanho in tamanhos:
    start = time.perf_counter()
    cavalo = Cavalo(tamanho)
    cavalo.tabuleiro[0][0] = 0
    cavalo.resolver(0, 0, 1)
    end = time.perf_counter()
    print(f"Tempo de execução da força bruta: {end - start:.6f} segundos")


#Ex12
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("Problema do caixeiro:")
resultado = held_karp(distancias)
print(f"Distância mínima (Held-Karp): {resultado}")


caminho, distancia = vizinho_mais_proximo(distancias)
print(f"Caminho (Vizinho Mais Próximo): {caminho}")
print(f"Distância total: {distancia}")

solucao, distancia = algoritmo_genetico(distancias)
print(f"Solução (Algoritmo Genético): {solucao}")
print(f"Distância total: {distancia}")