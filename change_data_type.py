#Change data type of given numpy array

import numpy as np

arr=np.array([[1,2,3,4,5]])
print(arr)
print(arr.dtype)

arr=arr.astype('float64')
print(arr)

print(arr.dtype)


"""
NumPy astype() Method
The numpy.astype() method is used to change the data type NumPy array from one data type to another.

The function takes an argument which is the target data type. The function supports all the generic types and built-in types of data.

"""