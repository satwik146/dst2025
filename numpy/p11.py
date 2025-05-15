import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a3 = np.array([7, 8, 9])
a4=np.ones([3,5])   

print(np.hstack((a1, a2, a3)))  
print(np.vstack((a1, a2, a3))) 

print(np.column_stack((a1, a2)))