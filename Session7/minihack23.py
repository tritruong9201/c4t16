while True:
    n=int(input("Enter number: "))
    if n>0:
        for i in range(1,n+1,2):
            print(i)
        break
    else:
        continue