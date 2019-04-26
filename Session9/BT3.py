sum=0
value_user = input("Enter a list of numbers, seperate by ',': ")
this_list = value_user.split(",")
print(*this_list)

# n=int(input("Enter a number: "))
# for i in range(0,len(this_list)-1):
#     if n == this_list[i]:
#         print("Found, position",i+1)
#         break
#     else:
#         print("Not found in our list")

for i in range(len(this_list)):
    sum = sum + int(this_list[i])
print(sum)