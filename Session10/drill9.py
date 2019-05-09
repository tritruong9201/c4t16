a=1
dict_list={
    "question":"How many legs an octopus has: ",
    "answer" : ["One leg","Two legs","Four legs","Eight legs"]
}
print(dict_list["question"])
x=dict_list["answer"]
for i, item in enumerate(x):
    print(i+1, ".",item)
while True:
    n=int(input("Enter your answer: "))
    Rightanswer="Eight legs"
    if n<1 or n>4:
        print("Enter again")
    else:
        if x[n-1]==Rightanswer:
            print("True")
            break
        else:
            print("False")
            a+=1
print(a)