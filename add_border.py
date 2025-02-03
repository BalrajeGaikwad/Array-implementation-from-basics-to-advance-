# How to add a border around a NumPy array?

"""
Sometimes we need to add a border around a NumPy matrix. Numpy provides a function known as ‘numpy.pad()’ to construct the border
"""
import numpy as np 

arr1=np.ones((2,2))
print("original array")
print(arr1)

print("\n0 on the border and 1 inside the array")

array=np.pad(arr1 , pad_width=1 ,mode='constant', constant_values=0)

print(array)


# syntax::  numpy.pad(array, pad_width, mode='constant', **kwargs)  


import numpy as np
arr2=np.zeros((3,3))
print("original Array ")
print(arr2)

print("\n1 on the border and 0 inside the array")
array1=np.pad(arr2,pad_width=1, mode='constant',constant_values=1)
print(array1)