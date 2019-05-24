map={
    "X" : 4,
    "Y" : 4,
}
K={
    "X" : 2,
    "Y" : 1,
}
K2={
    "X" : 0,
    "Y" : 0,
}
P={
    "X" : 1,
    "Y" : 2,
}
E={
    "X" : 3,
    "Y" : 2,
}
W={
    "X" : 2,
    "Y" : 2,
}
key_storage=0
key_storage_2=0
while True:
    for y in range(map["Y"]):
        for x in range(map["X"]):
            if P["X"]==x and P["Y"]==y:
                print("P",end=" ")
            elif K["X"]==x and K["Y"]==y:
                if key_storage==1:
                    print("-",end=" ")
                else:
                    print("K",end=" ") 
            elif K2["X"]==x and K2["Y"]==y:
                if key_storage_2==1:
                    print("-",end=" ")
                else:
                    print("K",end=" ")
            elif E["X"]==x and E["Y"]==y:
                print("E",end=" ")
            elif W["X"]==x and W["Y"]==y:
                print("W",end=" ")
            else:
                print("-",end=" ")
        print(" ")
    if P["X"]==E["X"] and P["Y"]==E["Y"]:
        if key_storage==1:
            if key_storage_2==1:
                print("CONGRATS, YOU HAVE JUST ESCAPED THE DUNGEON")
                break
            else:
                print("YOU NEED KEYS TO ESCAPE")
        else:
            print("YOU NEED KEYS TO ESCAPE")
    yourmove=input("Your move: ").upper()
    dx=0
    dy=0
    if yourmove=="W":
        dy=-1
    elif yourmove=="S":
        dy=1
    elif yourmove=="A":
        dx=-1
    elif yourmove=="D":
        dx=1
    else:
        print("INVALID")
    if 0<=P["X"]+dx<map["X"] and 0<=P["Y"]+dy<map["Y"]:
        if P["X"]+dx!=W["X"] or P["Y"]+dy!=W["Y"]:
            P["X"]+=dx
            P["Y"]+=dy
    if P["X"]==K["X"] and P["Y"]==K["Y"]:
        key_storage+=1
        print("YOU HAVE JUST PICKED A KEY")
    if P["X"]==K2["X"] and P["Y"]==K2["Y"]:
        key_storage_2+=1
        print("YOU HAVE JUST PICKED A KEY")