#  Assignment 4: take student detail and store in dictionary 
student={
    "Name":input("Enter your name="),
    "Age":int(input("Enter your age=")),
    "Course":input("Enter your course="),
    "College":input("Enter your college=")
}
print(student)

for key,value in student.items():
    print(key,value)