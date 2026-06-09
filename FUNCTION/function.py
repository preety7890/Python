# create function to check even/odd
def checkEvenOdd(num):
    if num%2==0:
        print("NUmber is Even..")
    else:
        print("Number is odd...")

num=int(input("Enter your number:"))
result=checkEvenOdd(num)


# create function to find largest of two numbers..

def LargestNumber(a,b):
    if a>b:
        print (a," is largest than",b )
    elif b>a:
        print(b,"is largest than",a)
    else:
        print("Both number are equal..")

a=int(input("Enter first value:"))
b=int(input("Enter second number:"))
LargestNumber(a,b)