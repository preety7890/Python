# create email validator..

email=input("Enter your email: ")
if email.endswith(".com"):
    print("Valid email..")
else:
    print("Invalid email...")