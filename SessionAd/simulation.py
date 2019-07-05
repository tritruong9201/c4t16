from queue import Queue
import random
class Simulation:
    def __init__(self,process_rate,min_req_rate,max_req_rate):
        self.process_rate=process_rate
        self.min_req_rate=min_req_rate
        self.max_req_rate=max_req_rate
    def run(self,test_number):
        n=0
        for i in range(test_number):
            req_rate=random.randint(self.min_req_rate,self.max_req_rate)
            if req_rate>self.process_rate:
                n += req_rate - self.process_rate
        lost_requests_rate = n/test_number
        return lost_requests_rate