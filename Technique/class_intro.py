class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "Day la mot doan string"
person=Person("Tri","18")
print(person.__str__())