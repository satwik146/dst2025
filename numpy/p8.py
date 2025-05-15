import numpy as np

arr= np.arange(1, 10)
arr2= np.arange(2, 25, 2)

arr3=arr.reshape(3,-1)
arr4=arr2.reshape(4,-1)
print(arr3,'\n')
print(arr4,'\n')