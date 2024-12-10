#find the grade and gpa from a mark

mark=float(input("Enter your marks: "))

if mark>80:
    print("Grade: A+ and GPA: 4.00")
elif 75<=mark<80:
    print("Grade: A and GPA: 3.75")
elif 70<=mark<75:
    print("Grade: A- and GPA: 3.50")
elif 65<=mark<70:
    print("Grade: B+ and GPA: 3.25")
else:
    print("falied")