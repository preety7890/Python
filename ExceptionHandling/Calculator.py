# create calculator and  handle division by zero

def calculator(num1,num2,operator):
 if operator == "+":

    print("Addition of two number is:",num1+num2)
  
 elif operator == "-":
    print("Subtraction of two number is:",num1-num2)

 elif operator == "*":
    print("Multiplication of two number is:",num1*num2)

 else:
    try:
        print("Division of two number is:",num1/num2)
    except ZeroDivisionError:
     print("Number can not be divide by zero...")


num1=int(input("Enter your number 1:"))
num2=int(input("Enter your number 2:"))
operator=input("Enter your operator(+,-,*,/):")
result=calculator(num1,num2,operator)
print(result)

