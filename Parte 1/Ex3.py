from Trie import Trie

livros = [
        "O Senhor dos Anéis",
        "Harry Potter e a Pedra Filosofal",
        "O Hobbit",
        "O Grande Gatsby",
        "1984",
        "A Guerra dos Tronos"
    ]
trie_livros = Trie()
for livro in livros:
        trie_livros.insert(livro)

prefixo = "O S"
print(f"Títulos que começam com '{prefixo}': {trie_livros.starts_with(prefixo)}")

prefixo = "A G"
print(f"Títulos que começam com '{prefixo}': {trie_livros.starts_with(prefixo)}")

print("Teste de correção automática com distância de edição:")
titulo_testado = "O Senho dos Anéis"
max_distancia = 2
sugestoes = trie_livros.suggest_corrections(titulo_testado, max_distancia)
print(f"Sugestões de correção para '{titulo_testado}': {sugestoes}")

titulo_testado = "Harry Poter e a Pedra Filosofal"
sugestoes = trie_livros.suggest_corrections(titulo_testado, max_distancia)
print(f"Sugestões de correção para '{titulo_testado}': {sugestoes}")