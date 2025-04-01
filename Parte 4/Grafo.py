from collections import deque

class Grafo:
    def __init__(self):
        self.grafo_lista = {}
        self.grafo_matriz = []
        self.vertices = []
        self.num_vertices = 0

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            self.num_vertices += 1

            for linha in self.grafo_matriz:
                linha.append(0)
            self.grafo_matriz.append([0] * self.num_vertices)

    def adicionar_aresta(self, origem, destino, peso=1, direcionado=False):
        if origem not in self.grafo_lista:
            self.grafo_lista[origem] = []
        if destino not in self.grafo_lista:
            self.grafo_lista[destino] = []

        if (destino, peso) not in self.grafo_lista[origem]:
            self.grafo_lista[origem].append((destino, peso))

        if not direcionado and (origem, peso) not in self.grafo_lista[destino]:
            self.grafo_lista[destino].append((origem, peso))

        origem_index = self.vertices.index(origem)
        destino_index = self.vertices.index(destino)
        self.grafo_matriz[origem_index][destino_index] = peso

        if not direcionado:
            self.grafo_matriz[destino_index][origem_index] = peso

    def mostrar_lista(self):
        print("\nLista de Adjacência:")
        for bairro, conexoes in self.grafo_lista.items():
            print(f"{bairro}: {conexoes}")

    def mostrar_matriz(self):
        print("\nMatriz de Adjacência:")
        print("   ", end="")
        for vertice in self.vertices:
            print(f" {vertice} ", end=" ")
        print()

        for i in range(self.num_vertices):
            print(f"{self.vertices[i]} ", end="")
            for j in range(self.num_vertices):
                print(f"{self.grafo_matriz[i][j]:3}", end=" ")
            print()

    def mostrar(self):
        self.mostrar_lista()
        self.mostrar_matriz()

    def bfs(self, inicio):
        if inicio not in self.vertices:
            print("Vértice não encontrado!")
            return

        visitados = set()
        fila = deque([inicio])
        resultado = []

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                resultado.append(vertice)
                for vizinho, _ in self.grafo_lista.get(vertice, []):
                    if vizinho not in visitados:
                        fila.append(vizinho)
        print("BFS:", " -> ".join(resultado))

    def dfs(self, inicio):
        if inicio not in self.vertices:
            print("Vértice não encontrado!")
            return

        visitados = set()
        resultado = []

        def dfs_recursivo(vertice):
            visitados.add(vertice)
            resultado.append(vertice)
            for vizinho, _ in self.grafo_lista.get(vertice, []):
                if vizinho not in visitados:
                    dfs_recursivo(vizinho)

        dfs_recursivo(inicio)
        print("DFS:", " -> ".join(resultado))
