list1 = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
list2 = [150300, 247100, 333300, 266800, 420900, 318000]
max=list2[0]
min=list2[0]
#find max
for x in list2:
    if x>max:
        max=x
print(max)
for i in range(len(list2)):
    if list2[i]==max:
        print(i+1)
        print(list1[i])
#find min
for x in list2:
    if x<min:
        min=x
print(min)
for i in range(len(list2)):
    if list2[i]==min:
        print(i+1)
        print(list1[i])
