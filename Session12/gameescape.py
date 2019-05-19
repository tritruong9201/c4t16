map={
    "X" : 4,
    "Y" : 4,
}
K={
    "X" : 2,
    "Y" : 1,
}
P={
    "X" : 1,
    "Y" : 2,
}
E={
    "X" : 3,
    "Y" : 2,
}
key_storage_K=0
key_storage_E=0
key_storage_E_1=0
while True:
    for y in range(map["Y"]):
        for x in range(map["X"]):
            P_is_here=False
            if P["X"]==x and P["Y"]==y:
                P_is_here=True
            K_is_here=False
            if K["X"]==x and K["Y"]==y:
                K_is_here=True
            if K_is_here:
                if P["X"]==K["X"] and P["Y"]==K["Y"]:
                    key_storage_K=1
            E_is_here=False
            if E["X"]==x and E["Y"]==y:
                E_is_here=True
            if E_is_here:
                if P["X"]==E["X"] and P["Y"]==E["Y"]:
                    if key_storage_K==1:
                        key_storage_E=1
                    else:
                        key_storage_E_1=1
            
            if P_is_here:
                print("P",end=" ")
            elif K_is_here:
                if key_storage_K==1:
                    print("-",end=" ")
                else:
                    print("K",end=" ")    
            elif E_is_here:
                print("E",end=" ")
            else:
                print("-",end=" ")
        print(" ")

    # how to move
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
        P["X"]+=dx
        P["Y"]+=dy