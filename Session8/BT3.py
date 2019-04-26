import random
from random import shuffle
this_list=["captain america", "iron man", "thor", "hulk", "hawkeye", "black widow"]
print(*this_list)
i=random.randint(0,len(this_list)-1)
this_list[i]=this_list[i].upper()
list1 = list(this_list[i])
shuffle(list1)
print(*list1)
x=str(input("Enter the character name: "))
if x == this_list[i].lower():
    print("Correct")
else:
    print("Wrong")