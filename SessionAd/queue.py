class Queue:
    def __init__(self):
        self.items=[]
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
        self.items.insert(0,item)
    def remove(self):
        return self.items.pop()
