this_list=["captain america", "iron man", "thor", "hulk", "hawkeye", "black widow"]
print(*this_list)
while True:
    crud=str(input("Choose C, R, U, D: "))
    if crud == "C":
        new_item=str(input("Enter new item: "))
        this_list.append(new_item)
        print(*this_list)
        break
    elif crud == "R":
        for x in this_list:
            print(x)
        break
    elif crud == "U":
        i = int(input("Enter place: "))
        j=i-1
        replacing_item=str(input("Enter new character: "))
        this_list[j]=replacing_item
        print(*this_list)
        break
    elif crud == "D":
        i = int(input("Enter place: "))
        j=i-1
        this_list.pop(j)
        print(*this_list)
        break
    else:
        print("Choose again")
        