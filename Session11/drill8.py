import random
list_dict = [
    {
        "Name" : "Tackle",
        "Minimum level" : 1,
        "Damage" : 5,
        "Hit rate" : 0.3,
    },

    {
        "Name" : "Quick attack",
        "Minimum level" : 2,
        "Damage" : 3,
        "Hit rate" : 0.5,
    },

    {
        "Name" : "Strong Kick",
        "Minimum level" : 4,
        "Damage" : 9,
        "Hit rate" : 0.2,
    }
]

# for i in range(0,len(list_dict)):
#     print("Skill",i+1)
#     for x in list_dict[i]:
#         print(x,":",list_dict[i][x])
#     print("-")

levelcharacter=random.randint(1,5)
hitrateper=random.randint(0,10)
hitrateper=hitrateper/10
print(hitrateper,"-","Level:",levelcharacter)
skillchoose=int(input("Choose skill number: "))
if skillchoose>3 or skillchoose<1:
    print("INVALID")
else:
    if skillchoose==1:
        print(list_dict[0]["Damage"])
        if hitrateper<list_dict[0]["Hit rate"]:
            print("Hit")
        else:
            print("Miss")
    elif skillchoose==2:
        if levelcharacter==1:
            print("Not Strong Enough")
        else:
            print(list_dict[1]["Damage"])
            if hitrateper<list_dict[0]["Hit rate"]:
                print("Hit")
            else:
                print("Miss")
    else:
        if levelcharacter>=4:
            print(list_dict[2]["Damage"])
            if hitrateper<list_dict[0]["Hit rate"]:
                print("Hit")
            else:
                print("Miss")
        else:
            print("Not Strong Enough")
