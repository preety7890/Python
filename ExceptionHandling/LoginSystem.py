# create login system with custom exception

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "preety" or password != "246hk":
        raise Exception("Login Failed")

    print("Login Successful")

except Exception as e:
    print(e)