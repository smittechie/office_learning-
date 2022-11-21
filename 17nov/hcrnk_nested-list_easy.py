# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.



students  = [["aman",20.0],["amit",37.2],["rohan",57.0],['Tina', 37.2],["sharda",75.0]]

# students = [i for i in students if i[1] == sorted(set([j[1] for j in students]))[1]]
# print("\n".join(sorted([i[0] for i in students])))


##self
sort_student=sorted(students,key = lambda a : (a[1]),reverse=False)
print(sort_student)

first_element = sort_student[0]
poped = sort_student.pop([0][0])
sort_student.insert(2,poped)

print(sort_student[0][0],
      "\n",
      sort_student[1][0])

