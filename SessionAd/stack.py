class Stack:
    def __init__(self):
        self.items = []
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
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def clear(self):
        self.items=[]