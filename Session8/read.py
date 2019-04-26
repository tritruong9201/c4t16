import random
this_list = ["lion", "bear", "wolf"]
print(this_list)
new_item=input("Enter an animal: ")
this_list.append(new_item)
print(this_list)
print(*this_list, sep = " ")
i=random.randint(0,len(this_list)-1)
print(i)
print(this_list[i])
n1 = this_list[0].upper()
n2 = this_list[len(this_list)-1].upper()
n3 = this_list[len(this_list)-2].upper()
print(n1,n2,n3)