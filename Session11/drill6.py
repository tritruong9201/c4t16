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
number1=int(input("Enter a number: "))
dict2["ACER"]=number1
print(dict2)

sum=0

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
print(dict1)

for x in dict1:
    sum=dict1[x]*dict2[x]
print(sum)