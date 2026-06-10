# create file name student.txt and store name,age college
name = input("Enter your name:")
age=  input("Enter your age:")
college=input("Enter your college name:")

file=open("student.txt","w")


file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n") 
file.write("College: " + college + "\n")


file.close()