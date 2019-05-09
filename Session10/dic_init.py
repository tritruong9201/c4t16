n=input("Enter your name: ")
m=input("Enter your age: ")
p=input("Enter your school: ")
dict1={
    "name": n, 
    "age": m, 
    "school": p
}
print(dict1 == {})
print(dict1)
# for x in list1:
#     print(list1[x],x)
a=input("Enter name, age, or school:")
del dict1[a]
print(dict1)
