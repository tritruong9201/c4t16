from stack import Stack

class StringProcessor:
    def __init__(self):
        pass

    def reverse(self,string):
        stack=Stack()
        for s in string:
            stack.push(s)
        re=""
        while stack.is_empty()==False:
            re+=stack.pop()
        return re

    def binary_string(self,string):
        stack=Stack()
        while string>0:
            if string%2==0:
                stack.push(0)
                string=string/2
            else:
                stack.push(1)
                string=(string-1)/2
        nu=""
        while stack.is_empty()==False:
            nu+=str(stack.pop())
        return nu

    def process_sequence(self,string):
        stack=Stack()
        result=""
        for s in string:
            if s =="*":
                result+=stack.pop()
            else:
                stack.push(s)
        return s

    def is_balanced(self,string):
        stack=Stack()
        i1=0
        i2=0
        i3=0
        j1=0
        j2=0
        j3=0
        bool1=False
        for s in string:
            if s=="{":
                i1+=1
            elif s=="}":
                j1+=1
            elif s=="[":
                i2+=1
            elif s=="]":
                j2+=1
            elif s=="(":
                i3+=1
            else:
                j3+=1
        if i1==j1 and i2==j2 and i3==j3:
            bool1=True
        return bool1