def UCLN(a,b):
    if b==0:
        return a
    else:
        q=a//b
        r=a-b*q
        return UCLN(b,r)
a=int(input())
b=int(input())
if b>a:
    c=b
    b=a
    a=c
print(UCLN(a,b))