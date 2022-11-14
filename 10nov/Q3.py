#WAP to return the grade of the given mark.

'''''
More than 90 is A+ grade
90 to 81 is A
80 to 71 is B
70 to 61 is C
60 to 50 is D
Below 50 are Fail
	Example: 
		Input 30
		Output : You are fail
		Input 55
		Output : your grade is D
'''''
marks = int(input("enter the marks: "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
elif marks <= 50:
    print("Fail")