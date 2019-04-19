month=int(input("Enter month: "))
while True:
    if month<1 or month>13:
        print("Khong hop le")
    else:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            print("31")
            
        elif month == 2:
            print("28 hoac 29")
            
        else:
            print("30")
            
    break