sum=0
dict_list=[
{
    "name" : "Huy",
    "role" : "Waiter",
    "hours" : 12,
    "salary per hour" : 0.8
},

{
    "name" : "Tung",
    "role" : "Cook",
    "hours" : 24,
    "salary per hour" : 1.5
},

{
    "name" : "M.Duc",
    "role" : "Manager",
    "hours" : 20,
    "salary per hour" : 2
}
]
print(dict_list)
p1={
    "name" : "Don",
    "role" : "Waiter",
    "hours" : 12,
    "salary per hour" : 0.9
}
p2={
    "name" : "H.Duc",
    "role" : "Waiter",
    "hours" : 14,
    "salary per hour" : 0.7
}
dict_list.append(p1)
dict_list.append(p2)
print(dict_list)
print(dict_list[2]["salary per hour"])
dict_list[0]={
    "name" : "Huyen",
    "role" : "Waitress",
    "hours" : 14,
    "salary per hour" : 1
}
print(dict_list)
del dict_list[len(dict_list)-1]
print(dict_list)
for i in range(0,len(dict_list)):
    for x in dict_list[i]:
        print(x,": ",dict_list[i][x],", ",end=" ")
    print(" ")
for i in range(0,len(dict_list)):
    print("Name: ",dict_list[i]["name"],"/", "Salary: ", dict_list[i]["salary per hour"]*dict_list[i]["hours"])
for i in range(0,len(dict_list)):
    sum=sum+dict_list[i]["salary per hour"]*dict_list[i]["hours"]
print(sum)