from KnightsTour import Cavalo, CavaloHeuristica
import time

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
