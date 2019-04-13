while True: 
    n=input("Enter your password: ")
    if n.isalpha() or len(n)<=8:
        print("Mat khau khong hop le")
    else: 
        print ("Mat khau hop le")
        break