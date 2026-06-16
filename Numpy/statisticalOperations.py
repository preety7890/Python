# create monthly sales array calculate total sales , average sale

import numpy as np

sales=np.array([20000,21000,56000,45000,35000,26000,43000,52000,40000])
# indexing
print(sales[0])  # 20000
print(sales[-1]) # 40000
# slicing
print(sales[1:4]) # 21000,56000,45000
 # shape 
print(sales.shape)

print("Total sales is:",np.sum(sum))
print("Average sales is:",np.mean(sales))
print("Highest sales:",np.max(sales))
print("Lowest sales:",np.min(sales))

print("All sales increases with 10% is:" , sales*1.10)


      
