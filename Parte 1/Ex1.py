from Scheduler import Scheduler

task_scheduler = Scheduler()
task_scheduler.add(1, 5, 2)
task_scheduler.add(2, 3, 1)
task_scheduler.add(3, 8, 3)

print("Tarefa Procesada:" ,task_scheduler.execute_next())
task_scheduler.modify_priority(3, 0)
print("Tarefa processada após atualização:", task_scheduler.execute_next())