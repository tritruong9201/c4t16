from random import shuffle
value_user = str(input("Enter a word: ")).upper()
this_list = list(value_user)
shuffle(this_list)
print(*this_list)