import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[-1])         #array access
print(arr[2:6])
print(arr[::2])
print(arr[::-3])

copy = arr[2:6]
print(copy)

print(arr[[1,2,6]])  #FANCY INDEXING
ind = [2,3,6]

print(arr[ind])
bol = [false, true, false,  false, true, false, true, true, false]
print(rre[bol]) #FILTERING/BOOLEAN MASKING

arr2 = arr.reshape((3,3))

print(arr2)
print(arr2.ndim)

arr3 = arr.flatten()
print(arr3 , arr3.ndim)



