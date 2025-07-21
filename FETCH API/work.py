import numpy as np

arr = [2,4,6,8]
arr2 = np.array([2,3,5,6,7,8,9,6,5,3,])
arr3 = np.array([4,5,6,8] , [3,6,8,9])

copy = np.insert(arr , 2, 25)
print(arr3)

copy = np.insert(arr3, 0 , 78 , axis=0)
copy = np.append(arr , 56)
copy = np.delete(arr3 ,0, axis1)

copy = np.concatenate((arr , arr2))

copy= np.split(arr2 , 2)

print(copy)