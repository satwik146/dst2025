import numpy as np

arr= np.arange(1, 10)
print(arr,'\n')

arr=arr.reshape(3,3)        
print(arr,'\n')

arr=arr.reshape(9)
print(arr,'\n')

arr= arr.reshape(9,1)
print(arr)

arr= arr.reshape(1,9)
print(arr)

