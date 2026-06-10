# student registration system using file handling 
# 1. add student 2.saved to files 3. read student 4. display all records

while True:
    print("===== Student Registration System =====\n")
    print("1. Add Student Details\n")
    print("2. Save File\n")
    print("3. Read Student Details\n")
    print("4. Exit\n")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter your Name: ")
        rollno = input("Enter your Roll No: ")
        email = input("Enter your Email: ")
        address = input("Enter your Address: ")

        print("Student added successfully...")

    elif choice == "2":
        try:
            with open("StudentRegistration.txt", "a") as file:
                file.write("Name: " + name + "\n")
                file.write("Roll No: " + rollno + "\n")
                file.write("Email: " + email + "\n")
                file.write("Address: " + address + "\n")
                file.write("-------------------------\n")

            print("Student saved successfully...")

        except NameError:
            print("First fill student details using Option 1.")

    elif choice == "3":
        try:
            with open("StudentRegistration.txt", "r") as file:
                data = file.read()
                print("\nStudent Records:")
                print(data)

        except FileNotFoundError:
            print("No records found. Save a student first.")
   

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")


       
    
 
