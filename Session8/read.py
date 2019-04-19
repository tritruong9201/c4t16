import random
this_list = ["lion", "bear", "wolf"]
print(this_list)
new_item=input("Enter an animal: ")
this_list.append(new_item)
print(this_list)
print(*this_list)
i=random.randint(0,len(this_list))
print(this_list[i])
