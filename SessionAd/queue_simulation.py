import random
from queue import Queue
class QueueSimulation:
    def __init__(self, process_rate, min, max, capacity):
        self.process_rate = process_rate
        self.min_req_rate = min
        self.max_req_rate = max
        self.capacity = capacity
        self.queue = Queue(self.capacity)

    def step(self,requests):
        self.requests = requests
        results, lost_count = [], 0
        while self.queue.is_empty() == False:
            results.append(self.queue.remove())
            
        l = len(results)
        for i in range(len(self.requests)):
            if i < self.process_rate - l:
                results.append(self.requests[i])
            elif i >= self.process_rate - l and i < self.process_rate - l + self.capacity:
                self.queue.insert(self.requests[i])     
            else:
                lost_count += 1
        return results, lost_count

    def run(self,times):
        self.times = times
        lost_requests = []
        du = 0
        for i in range(times):
            req_rate = random.randint(self.min_req_rate, self.max_req_rate)
            if du + req_rate <= self.process_rate:
                lost_requests.append(0) 
            else:
                du = req_rate - self.process_rate + du
                if du > self.capacity:
                    lost_requests.append(du - self.capacity)
                    du = self.capacity
                else:
                    lost_requests.append(0)
        tong = 0
        for l in lost_requests:
            tong += l
        return tong/times