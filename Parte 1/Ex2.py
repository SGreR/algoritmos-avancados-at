from Scheduler import Scheduler

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