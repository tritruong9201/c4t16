from stack import Stack
class StringProcessor:
    def reverse(self,string):
        stack=Stack()
        for s in string:
            stack.push(s)
        res=""
        while stack.is_empty()==False:
            res+=stack.pop()
        return res
p=StringProcessor()
print(p.reverse("abc"))