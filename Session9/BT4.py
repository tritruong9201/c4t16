this_list = [5, 1, 8, 92, 7, 30]
this_list1 = []
for x in this_list:
    if x%2==0:
        this_list1.append(x)
print(*this_list1, sep=",")