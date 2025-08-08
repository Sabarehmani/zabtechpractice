import numpy as np 
arr = np.array([2,4,5,6, np.nan, 6,7])
arr2 = np.nan_to_num(arr , nan=22)
print(np.isnan(arr2))
print(arr2)

arr = np.array([2,3,4 np.inf,5,6, -np.inf])
print(np.isinf(arr))

arr2 = np.nan_to_num(arr, posinf=20, neginf=40)
print(np.isinf(arr2))
print(arr2)

import pandas as pd
data = {
    "name" : ["usman" , "adnan" , "saba" , "kamran"],
    "age" : [27,25,23,20]
}