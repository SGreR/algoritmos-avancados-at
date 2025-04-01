import itertools
import random

#Dinâmica
def held_karp(distancias):
    n = len(distancias)
    C = {}

    for k in range(1, n):
        C[(1 << k, k)] = distancias[0][k]

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            subset_mask = 0
            for i in subset:
                subset_mask |= 1 << i
            for k in subset:
                prev_subset_mask = subset_mask & ~(1 << k)
                min_dist = float('inf')
                for m in subset:
                    if m != k:
                        dist = C[(prev_subset_mask, m)] + distancias[m][k]
                        if dist < min_dist:
                            min_dist = dist
                C[(subset_mask, k)] = min_dist

    final_mask = (1 << n) - 1
    min_tour = float('inf')
    for k in range(1, n):
        dist = C[(final_mask ^ (1 << 0), k)] + distancias[k][0]
        if dist < min_tour:
            min_tour = dist

    return min_tour

#Gulosa

def vizinho_mais_proximo(distancias):
    n = len(distancias)
    visitado = [False] * n
    caminho = []
    total_distancia = 0
    cidade_atual = 0
    visitado[cidade_atual] = True
    caminho.append(cidade_atual)

    for _ in range(n - 1):
        cidade_mais_proxima = None
        menor_distancia = float('inf')

        for i in range(n):
            if not visitado[i] and distancias[cidade_atual][i] < menor_distancia:
                cidade_mais_proxima = i
                menor_distancia = distancias[cidade_atual][i]

        visitado[cidade_mais_proxima] = True
        caminho.append(cidade_mais_proxima)
        total_distancia += menor_distancia
        cidade_atual = cidade_mais_proxima

    total_distancia += distancias[cidade_atual][0]
    return caminho, total_distancia

#Genetico

def calcular_distancia(caminho, distancias):
    distancia = 0
    for i in range(len(caminho) - 1):
        distancia += distancias[caminho[i]][caminho[i+1]]
    distancia += distancias[caminho[-1]][caminho[0]]
    return distancia

def crossover(pai1, pai2):
    corte = random.randint(1, len(pai1) - 1)
    filho = pai1[:corte] + [cidade for cidade in pai2 if cidade not in pai1[:corte]]
    return filho

def mutacao(caminho):
    i, j = random.sample(range(len(caminho)), 2)
    caminho[i], caminho[j] = caminho[j], caminho[i]
    return caminho

def algoritmo_genetico(distancias, pop_size=100, generations=1000, mutation_rate=0.1):
    n = len(distancias)
    populacao = [random.sample(range(n), n) for _ in range(pop_size)]
    melhor_solucao = None
    melhor_distancia = float('inf')

    for geracao in range(generations):
        populacao.sort(key=lambda caminho: calcular_distancia(caminho, distancias))
        if calcular_distancia(populacao[0], distancias) < melhor_distancia:
            melhor_solucao = populacao[0]
            melhor_distancia = calcular_distancia(populacao[0], distancias)

        nova_populacao = populacao[:pop_size//2]  # Seleção de pais
        while len(nova_populacao) < pop_size:
            pai1, pai2 = random.sample(populacao[:pop_size//2], 2)
            filho = crossover(pai1, pai2)
            if random.random() < mutation_rate:
                filho = mutacao(filho)
            nova_populacao.append(filho)

        populacao = nova_populacao

    return melhor_solucao, melhor_distancia



