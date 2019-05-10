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
while True:
    for y in range(map["Y"]):
        for x in range(map["X"]):
            P_is_here=False
            if P["X"]==x and P["Y"]==y:
                P_is_here=True
            K_is_here=False
            if K["X"]==x and K["Y"]==y:
                sum=0
                if P["X"]==K["X"] and P["Y"]==K["Y"]:
                    sum+=1
                if sum<1:
                    K_is_here=True
            E_is_here=False
            if E["X"]==x and E["Y"]==y:
                E_is_here=True
            
            if P_is_here:
                print("P",end=" ")
            elif K_is_here:
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
    print(P["X"],P["Y"],"-",K["X"],K["Y"])
