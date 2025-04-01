class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._collect_words(next_node, prefix + char))
        return words

    def levenshtein_distance(self, word1, word2):
        len_word1, len_word2 = len(word1), len(word2)
        dp = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]

        for i in range(len_word1 + 1):
            dp[i][0] = i
        for j in range(len_word2 + 1):
            dp[0][j] = j

        for i in range(1, len_word1 + 1):
            for j in range(1, len_word2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        return dp[len_word1][len_word2]

    def suggest_corrections(self, word, max_distance=2):
        all_words = self._collect_words(self.root, "")
        suggestions = [w for w in all_words if self.levenshtein_distance(word, w) <= max_distance]
        return suggestions

    def interactive_search(self):
        current_prefix = ""
        while True:
            char = input("Digite uma ou mais letras para receber sugestões (ou pressione Enter para sair): ")
            if char == "":
                break
            current_prefix += char
            print(f"Prefixo: {current_prefix} -> {self.starts_with(current_prefix)}")
            current_prefix = ""
            suggestions = self.suggest_corrections(current_prefix)
            if suggestions:
                print(f"Sugestões de correção: {suggestions}")
            else:
                print("Nenhuma sugestão encontrada.")
