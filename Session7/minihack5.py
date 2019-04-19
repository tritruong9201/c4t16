import random
i=0
while True:
    a1=random.randint(-10,20)
    a2=random.randint(-10,20)
    bien=random.randint(-4,4)
    a3=a1+a2+bien
    print(a1,"+",a2,"=",a3)
    n=str(input("Nhap D hoac S: "))
    if n=="D":
        if a1+a2==a3:
            print("Dung")
            i+=1
        else:
            print("Sai")
            break
    elif n=="S":
        if a1+a2!=a3:
            print("Dung")
            i+=1
        else:
            print("Sai")
            break
    else: 
        break
print("Diem la: ",i)