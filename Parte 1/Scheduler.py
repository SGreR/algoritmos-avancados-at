from MinHeap import MinHeap

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