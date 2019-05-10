dict1={
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000,
}

dict2 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}
dict2["TOSHIBA"]=10
dict2["DELL"]=10
dict2["MACBOOK"]=2
dict2["FUJITSU"]=15
dict2["ALIENWARE"]=5

# print(dict1["ASUS"])
computerbrand=input("Enter a brand: ")
computerbrand=computerbrand.upper()
# print(dict1[computerbrand])
# x=dict1["ASUS"]
number1=int(input("Enter a number: "))
# print(number1*dict1[computerbrand])
dict2[computerbrand]=dict2[computerbrand]-number1
print(dict2)
for x in dict2:
    print(x,":",dict2[x],end=" ")
    print(" ")