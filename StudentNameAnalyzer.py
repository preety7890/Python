# create student name analyzer

name=input("Enter your name:")

print("Name= ",name)
print("Uppercase= ",name.upper())
print("Lowercase= ",name.lower())
print("Total length of words= ",len(name))
print("Title case= ",name.title())

vowels="aeiouAEIOU"
vowels_count=0
for i in name:
    if i in vowels:
     vowels_count=vowels_count+1

print("Total vowels in words is =",vowels_count)