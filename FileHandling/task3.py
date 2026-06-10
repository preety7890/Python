# append new details
name = input("Enter your name:")
age=input("Enter your age:")
college=input("Enter your college name:")

file=open("student.txt","a")


file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n") 
file.write("College: " + college)

file.close()
