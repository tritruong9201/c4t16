while True: 
    n=input("Enter your first name: ")
    m=input("Enter your last name: ")
    if m.isalpha() and n.isalpha():
        print(n,m)
        break
    else:
        continue