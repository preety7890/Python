# create student class store name age course display all details

class Students:

    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course



stud=Students("Priti Gupta",21,"BCA")
print(stud.name)
print(stud.age)
print(stud.course)


# create employee class store name,department,salary

class Employee:
    def __init__(self,name,department,salary):
      self.name=name
      self.department=department
      self.salary=salary
    
employee=Employee("Priti Gupta","Computer Application",20000)
print(employee.name)
print(employee.department)
print(employee.salary)