value_user = input("Enter your favorite things, seperated by ',': ")
this_list = value_user.split(",")
print(*this_list)
print("Your things: ")
for x in this_list: 
    print(x.upper())