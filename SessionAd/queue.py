class Queue:
    def __init__(self,capacity):
        self.items=[]
        self.capacity=capacity
    def __str__(self):
        x=""
        for i in range(0,len(self.items)):
            if i==0:
                x=x+str(self.items[i])
            else:
                x=x+" "+str(self.items[i])
        return x
    def is_empty(self):
        return self.items==[]
    def insert(self,item):
        bool1=False
        if len(self.items)<self.capacity:
            self.items.insert(0,item)
            bool1=True
        return bool1
    def remove(self):
        if self.items!=[]:
            return self.items.pop()
    def is_full(self):
        return len(self.items)==self.capacity