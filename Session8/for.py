this_list=["captain america", "iron man", "thor", "hulk", "hawkeye", "black widow"]
print(*this_list)
# for i in range(len(this_list)):
#     print(this_list[i])
# for item in this_list:
#     print(item)
for i, item in enumerate(this_list):
    print(i+1, ".",item.upper())
for x in this_list:
    if "e" in x:
        print(x.upper())