dict1 = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}
print(dict1)
sum=0
# print(dict1["MACBOOK"])
# computerbrand=input("Enter a brand: ")
# computerbrand=computerbrand.upper()
# print(dict1[computerbrand])
dict1["TOSHIBA"]=10
# print(dict1)
# computerbrand=input("Enter a brand: ")
# computernumber=input("Enter a number: ")
# dict1[computerbrand]=computernumber
# print(dict1)
dict1["DELL"]=10
dict1["MACBOOK"]=2
# print(dict1)
# for x in dict1:
#     sum=dict1[x]+sum
# print(sum)
dict1["FUJITSU"]=15
dict1["ALIENWARE"]=5
for x in dict1:
    print(x,":",dict1[x],end=" ")
    print(" ")