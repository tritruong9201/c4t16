this_list=["captain america", "iron man", "thor", "hulk", "hawkeye", "black widow"]
print(*this_list)
replacing_item=str(input("Enter your Marvel character: "))
i=int(input("Enter the place: "))
j=i-1
this_list[j]=replacing_item
print(*this_list)