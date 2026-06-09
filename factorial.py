num = int(input("enter your number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print(fact)
    
 # login credinetials
name=input("enter your name:")
password=input("enter your password:")

if name=="priti":
    if password=="2346":
        print("login sucessfully...")
    else:
        print("wrong password..")
else:
    print("incorrect username..")