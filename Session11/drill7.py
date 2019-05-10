character = {
    "Name" : "Light",
    "Age" : 17,
    "Strength" : 8,
    "Defense" : 10,
    "HP" : 100,
    "Backpack" : ["Shield", "Bread Loaf"],
    "Gold" : 100,
    "Level" : 2,
}
print(character)
character["Gold"]=character["Gold"]+50
print(character)
character["Backpack"].append("FlintStone")
print(character)
character["Pocket"]=["MonsterDex","Flashlight"]
print(character)