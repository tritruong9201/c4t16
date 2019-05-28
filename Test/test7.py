list1=[1,2,3,4,5]
for x in list1:
    print(x,end=" ")
print(" ")
new_number=int(input())
list1.insert(0,new_number)
for x in list1:
    print(x,end=" ")