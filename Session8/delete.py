this_list=["captain america", "iron man", "thor", "hulk", "hawkeye", "black widow"]
print(*this_list)
# i=int(input("Enter the place: "))
# j=i-1
# this_list.pop(j)
while True:
    delete_item=str(input("Enter delete character: "))
    if delete_item in this_list: 
        print("Yes")
        break
    else:
        print("No")
        continue
this_list.remove(delete_item)
print(*this_list)