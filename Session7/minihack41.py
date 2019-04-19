taikhoan=input("Enter account: ")
while True:
    matkhau=input("Enter password: ")
    if matkhau.isalpha() or len(matkhau)<=8:
        print("Please enter again")
        continue
    else:
        break
while True:
    email=input("Enter email: ")
    if "@" in email:
        if ".com" in email:
            break
        else:
            print("Enter again")
    else:
        print("Enter again")
while True: 
    matkhaunhaplai=input("Enter password again: ")
    if matkhaunhaplai==matkhau:
        break
    else:
        print("Worng password")
        continue
print("Log in succesful")
