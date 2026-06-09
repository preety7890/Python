# create student information functions

def studentInfo(name,rollNo,age,course):
    print("Student Information are....")
    print("Name=",name)
    print("RollNo=",rollNo)
    print("Age=",age)
    print("Course=",course)

name=input("Enter Name:")
rollNo=int(input("Enter roll number:"))
age=int(input("Enter age:"))
course=input("Enter course:")

studentInfo(name,rollNo,age,course)