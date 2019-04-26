list1 = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
list2 = [150300, 247100, 333300, 266800, 420900, 318000]
list3 = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
list4 = []
for i in range(len(list1)):
    x=list2[i]/list3[i]
    list4.append(x)
print(list4)
for x in list4:
    print(x/len(list4))