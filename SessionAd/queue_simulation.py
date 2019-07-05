from queue import Queue
import random
class QueueSimulation:
    def __init__(self,process_rate,min_req_rate,max_req_rate,capacity):
        self.queue=Queue(capacity)
        self.process_rate=process_rate
        self.min_req_rate=min_req_rate
        self.max_req_rate=max_req_rate
    def step(self,requests):
        result=[]
        lost_count=0
        can_process=self.process_rate
        while not self.queue.is_empty:
            if can_process>0:
                result.append(self.queue.remove())
                can_process-=1
        for request in requests:
            if can_process>0:
                result.append(request)
                can_process-=1
                print(result)
            else:
                self.queue.insert(request)
                print(self.queue)
                if not self.queue.insert(request):
                    lost_count+=1
                can_process-=1
        return result,lost_count
    def run(self,test_number):
        pass