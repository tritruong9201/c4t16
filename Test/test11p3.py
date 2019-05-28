def dayso(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return dayso(n-1)+dayso(n-2)
sum=int(input())
print(dayso(sum))