# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.



students  = [["aman",20.0],["amit",37.2],["rohan",57.0],['Tina', 37.2],["sharda",75.0]]
#
# students = [i for i in students if i[1] == sorted(set([j[1] for j in students]))[1]]
# print("\n".join(sorted([i[0] for i in students])))

b=sorted(students,key = lambda a : (a[1]),reverse=False)
print(b)


# def method1():
#     if __name__ =="__main__":
#         lst_score = []
#         lst_name_score = []
#
#         for _ in range(int(input("range : "))):
#             name = input("name : ")
#             score = float(input("score : "))
#             lst_score.append(score)
#             lst_name_score.append([name,score])
#
#
#     #sort the score
#     lst_score.sort()
#
#     #get minimum value
#     lowestscore= lst_score[0]
#
#     #get second minimum
#     for i in lst_score:
#         if i > lowestscore:
#             lowestscore = i
#             break
#     print(lowestscore)
#     lsresult =[]
#     #find the student have score = minval
#
#     for i in lst_name_score:
#         if i[1] == lowestscore:
#             lsresult.append(i[0])
#     print(lsresult)
#     lsresult.sort()
#     for a in lsresult:
#         print(a)
#
# method1()