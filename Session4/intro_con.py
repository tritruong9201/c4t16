month=int(input("Month: "))
if month<1 or month>12:
    print("Invalid")
elif month<=3:
    print("Spring")
elif month<=6:
    print("Summer")
elif month<=9:
    print("Autumn")
else:
    print("Winter")
print ("Bye")