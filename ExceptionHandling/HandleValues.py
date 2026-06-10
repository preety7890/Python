# Take student marks input handle invalid values
try:
   marks=int(input("Enter marks:"))
   print("Your marks is:",marks)

except ValueError:
   print("Enter a valid marks..")


# open file safely using try-except
try:
 file=open("SalesData.txt","r")
 print(file.read())

except FileNotFoundError:
  print("File does not exist....")