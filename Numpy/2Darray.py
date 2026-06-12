#  create a 2d array of student marks and display shape dimensions total elements
import numpy as np

marks=np.array([[30,24,21,18],
                [24,17,28,22]])

print("Shape of array is:",marks.shape)
print("Dimensions of array is:",marks.ndim)
print(marks)
print("Total elements in array is",np.size(marks))

