import heapq

def prim(grafo, inicio):
    mst = []
    custo_total = 0

    pq = [(0, inicio)]

    visitados = set()

    while pq:
        custo, vertice = heapq.heappop(pq)

        if vertice in visitados:
            continue

        visitados.add(vertice)

        mst.append((vertice, custo))
        custo_total += custo

        for vizinho, peso in grafo.get(vertice, []):
            if vizinho not in visitados:
                heapq.heappush(pq, (peso, vizinho))

    return mst, custo_total
