def floyd_warshall(grafo):
    nodes = list(grafo.keys())

    dist = {node: {n: float('inf') for n in nodes} for node in nodes}

    for node in nodes:
        dist[node][node] = 0
        for vizinho, peso in grafo[node]:
            dist[node][vizinho] = peso

    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist