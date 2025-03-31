import heapq

def dijkstra(grafo, inicio):
    distancias = {node: float('inf') for node in grafo}
    distancias[inicio] = 0
    pq = [(0, inicio)]

    while pq:
        distancia_atual, node_atual = heapq.heappop(pq)

        if distancia_atual > distancias[node_atual]:
            continue

        for vizinho, peso in grafo[node_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(pq, (distancia, vizinho))

    return distancias

def rota_dijkstra(grafo, inicio, fim):
    distancias = {node: float('inf') for node in grafo}
    distancias[inicio] = 0
    pq = [(0, inicio)]
    anteriores = {}

    while pq:
        distancia_atual, node_atual = heapq.heappop(pq)

        if node_atual == fim:
            caminho = []
            while node_atual:
                caminho.append(node_atual)
                node_atual = anteriores.get(node_atual)
            return list(reversed(caminho)), distancias[fim]

        if distancia_atual > distancias[node_atual]:
            continue

        for vizinho, peso in grafo[node_atual]:
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(pq, (distancia, vizinho))
                anteriores[vizinho] = node_atual

    return None, float('inf')