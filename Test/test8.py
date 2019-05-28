list1=[1,2,3,4,5]
bien1=input("H or T: ").upper()
if bien1=="H":
    list1.pop(0)
    print(*list1)
if bien1=="T":
    list1.pop()
    print(*list1)
    