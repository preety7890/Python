#  anlaysis marks using list
marks=[78,98,65,66,78,57]

for i in marks:
    print(i)

# list all method 
marks.append(90)
marks.insert(3,89)
marks.pop(3)
print(marks)

# assignment 1 . create list of 10 marks calculate sum , maximum,minimum

num=[1,2,3,4,5,6,4,8,12,21,13]
total=sum(num)
print("sum of all list is:",total)

maximum=max(num)
print("maximum number in list is:",maximum)

minimum=min(num)
print("minimum number in list is:",minimum)