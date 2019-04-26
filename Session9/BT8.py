list1=[45, 67, 56, 78,45,67,89]
new_item=int(input("Enter a new number: "))
list1.append(new_item)
list1.sort(reverse=True)
for i,item in enumerate(list1):
    if i<5:
        print(i+1,".",item)