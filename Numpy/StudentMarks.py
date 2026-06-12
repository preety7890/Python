# create an array of 10 students marks and calculate
# Total marks , Average marks , Highest marks , Lowest marks

import numpy as np
marks=np.array([56,89,76,55,76,71,90,63,48,88])

print("Total marks of student is:",np.sum(marks))
print("Average marks of student is:",np.mean(marks))
print("Highest marks in student is:",np.max(marks))
print("Lowest marks in student is:",np.min(marks))

