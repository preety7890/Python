# 1. create function to add two number
def add(num1,num2):
   return num1+num2

#add(4,5)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
result=add(num1,num2)
print(result)



# 2. create function to calculate area of rectangle

def AreaofRectangle(length,breadth):
     return length*breadth

length=int(input("Enter your length:"))
breadth=int(input("Enter your breadth:"))

area= AreaofRectangle(length,breadth)
print("Area of reactangle is:=",area)