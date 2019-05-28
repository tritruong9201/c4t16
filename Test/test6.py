list1=[1,2,3,4,5]
for x in list1:
    print(x,end=" ")
print(" ")
new_number=int(input())
list1.append(new_number)
for x in list1:
    print(x,end=" ")