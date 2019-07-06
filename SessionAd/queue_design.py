import random
from queue_simulation import QueueSimulation
i=1
while True:
    sim = QueueSimulation(5, 4, 7, i)
    if sim.run(10000)<=0.1:
        print(i)
        break
    else:
        print(i)
        i+=1