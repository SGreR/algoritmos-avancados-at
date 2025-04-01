from CaixeiroViajante import held_karp, vizinho_mais_proximo, algoritmo_genetico

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