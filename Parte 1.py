from MinHeap import MinHeap
from Trie import Trie

#Ex 1
class Process:
    def __init__(self, pid, execution_time, priority):
        self.pid = pid
        self.execution_time = execution_time
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"(pid={self.pid}, priority={self.priority}, execution_time={self.execution_time})"

class Scheduler:
    def __init__(self):
        self.heap = MinHeap()
        self.process_map = {}

    def add(self, pid, execution_time, priority):
        process = Process(pid, execution_time, priority)
        self.heap.insert(process)
        self.process_map[pid] = process

    def execute_next(self):
        if self.heap.is_empty():
            return "No processes to execute."
        process = self.heap.pop()
        del self.process_map[process.pid]
        return f"Executing {process}"

    def modify_priority(self, pid, new_priority):
        if pid in self.process_map:
            process = self.process_map[pid]
            self.heap.remove(process)
            process.priority = new_priority
            self.heap.insert(process)
        else:
            return "Process not found."

task_scheduler = Scheduler()
task_scheduler.add(1, 5, 2)
task_scheduler.add(2, 3, 1)
task_scheduler.add(3, 8, 3)

print("Tarefa Procesada:" ,task_scheduler.execute_next())
task_scheduler.modify_priority(3, 0)
print("Tarefa processada após atualização:", task_scheduler.execute_next())


#Ex 2
class PacketScheduler(Scheduler):
    pass

scheduler = PacketScheduler()
scheduler.add("P1", 3, 5)
scheduler.add("P2", 1, 2)
scheduler.add("P3", 2, 4)

print("Pacote processado:", scheduler.execute_next())
scheduler.modify_priority("P3", 0)
print("Pacote processado após atualização:", scheduler.execute_next())
print()

#Ex 3
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