dict_list={
    "Name" : "Avenger Endgame",
    "Year" : 2019,
    "Characters" : ["captain america", "thor", "iron man", "hulk"],
}
print(dict_list)
dict_list["Country"]="USA"
print(dict_list)
for k, v in dict_list.items():
    print(k,"-",v)
dict_list["Characters"]=["doctor strange", "spider man", "black panther", "star lord"]
print(dict_list)
dict_list["Characters 2"] = ["captain america", "thor", "iron man", "hulk"]
print(dict_list)
del dict_list["Characters"][0]
print(dict_list)
print(dict_list["Characters"][1])
for x in dict_list["Characters 2"]:
    print(x)
for x in dict_list: 
    if x == "Characters 1":
        for i in range(0, len(dict_list["Characters 1"])):
            print(x,"-",dict_list[x][i])
    elif x == "Characters":
        for i in range(0, len(dict_list["Characters"])):
            print(x,"-",dict_list[x][i])
    else:
        print(x,"-",dict_list[x])