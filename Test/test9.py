def quadro(a,b,c):
    delta=b*b-4*a*c
    if delta>=0:
        deltamoi=delta**(1/2)
        x1=(-b+deltamoi)/(2*a)
        x2=(-b-deltamoi)/(2*a)
        print(x1,x2)
    else:
        print("Phuong trinh vo nghiem")
a=int(input())
b=int(input())
c=int(input())
quadro(a,b,c)