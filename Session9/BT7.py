list1=[45, 67, 56, 78]
for i,item in enumerate(list1):
    print(i+1,".",item)
new_item=int(input("Enter a new number: "))
list1.append(new_item)
for i,item in enumerate(list1):
    print(i+1,".",item)