# create calculator using conditions
num1=float(input("Enter your first number:"))
operator=input("Enter your operator(+,-,*,/):")
num2=float(input("Enter your second number:"))

if operator=="+":
    print(num1+num2)
elif operator=="-":
 print(num1-num2)
elif operator=="*":
   print(num1*num2)
else:  
 print(num1/num2)

# print table of any number

num=int(input("Enter your number:"))
for i in range(1,11):
  print(num ,"*",i,"=",num*i)

# print odd even number
a=int(input("enter your number:"))
if a%2==0:
  print(a,"is even number")
else:
  print(a,"is odd number:")
