# create employee management file

emp_id = (input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = (input("Enter Salary: "))

file = open("employee.txt", "a")

file.write("Employee ID: " + emp_id + "\n")
file.write("Name: " + name + "\n")
file.write("Salary: " + salary + "\n")
file.write("____________________________\n")


file.close()