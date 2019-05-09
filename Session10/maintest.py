# import random
# l=0
# dict_list=[
#     {
#         "question" : "1+1= ",
#         "answer" : [2,3,4,5],
#     },

#     {
#         "question" : "2+4= ",
#         "answer" : [6,7,8,9],
#     },

#     {
#         "question" : "4+6= ",
#         "answer" : [10,11,12,13],
#     }
# ]
# while True:
dict1={}
createquestion=str(input("Enter a question: "))
createanswer=input("Enter your choices, seperated by ',': ")
rightans=input("Enter the right answer: ")
list1=createanswer.split(",")
dict1["question"]=createquestion
dict1["answer"]=list1
print(dict1)


# n=random.randint(0,2)
# print(dict_list[n]["question"])
# for i, item in enumerate(dict_list[n]["answer"]):
#     print(i+1, "-",item)
# m=int(input("Enter your answer: "))
# Rightanswer = [2,6,10]
# if dict_list[m-1]["answer"] in Rightanswer:
#     print("True")
#     l+=1
# dict_list.remove(dict_list[n])

