class Cavalo:
    def __init__(self, n):
        self.n = n  # Tamanho do tabuleiro
        self.tabuleiro = [[-1 for _ in range(n)] for _ in range(n)]
        self.movimentos = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                           (2, 1), (1, 2), (-1, 2), (-2, 1)]

    def valido(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.tabuleiro[x][y] == -1

    def imprimir_tabuleiro(self):
        for i in range(self.n):
            print(self.tabuleiro[i])

    def resolver(self, x, y, passo):
        if passo == self.n * self.n:
            return True

        for dx, dy in self.movimentos:
            novo_x, novo_y = x + dx, y + dy
            if self.valido(novo_x, novo_y):
                self.tabuleiro[novo_x][novo_y] = passo
                if self.resolver(novo_x, novo_y, passo + 1):
                    return True
                self.tabuleiro[novo_x][novo_y] = -1  # Backtracking

        return False

class CavaloHeuristica:
    def __init__(self, n):
        self.n = n
        self.tabuleiro = [[-1 for _ in range(n)] for _ in range(n)]
        self.movimentos = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                           (2, 1), (1, 2), (-1, 2), (-2, 1)]

    def valido(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.tabuleiro[x][y] == -1

    def imprimir_tabuleiro(self):
        for i in range(self.n):
            print(self.tabuleiro[i])

    def contar_movimentos_validos(self, x, y):
        contador = 0
        for dx, dy in self.movimentos:
            novo_x, novo_y = x + dx, y + dy
            if self.valido(novo_x, novo_y):
                contador += 1
        return contador

    def resolver(self, x, y, passo):
        if passo == self.n * self.n:
            return True

        movimentos_validos = []
        for dx, dy in self.movimentos:
            novo_x, novo_y = x + dx, y + dy
            if self.valido(novo_x, novo_y):
                movimentos_validos.append((novo_x, novo_y))

        movimentos_validos.sort(key=lambda pos: self.contar_movimentos_validos(pos[0], pos[1]))

        for novo_x, novo_y in movimentos_validos:
            self.tabuleiro[novo_x][novo_y] = passo
            if self.resolver(novo_x, novo_y, passo + 1):
                return True
            self.tabuleiro[novo_x][novo_y] = -1  # Backtracking

        return False



