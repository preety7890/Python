# store marks of 5 student and calculate average
total=0
file=open("marks.txt","w")

for i in range(1,6):
    marks=int(input("Enter marks of student " + str(i) +" ="))
    total=total+marks

    file.write("Student " + str(i) + " marks= " + str(marks) + "\n")
    
    average=total/5

print("Average marks is:", average)
file.write("Average marks of student is:" + str(average))
file.close()