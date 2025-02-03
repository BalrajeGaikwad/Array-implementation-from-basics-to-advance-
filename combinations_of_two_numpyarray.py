# How to build an array of all combinations of two NumPy arrays?

"""
Sometimes we need to find the combination of elements of two or more arrays. 
Numpy has a function to compute the combination of 2 or more Numpy arrays named as “numpy.meshgrid()“. 
This function is used to create a rectangular grid out of two given 
one-dimensional arrays representing the Cartesian indexing or Matrix indexing.


syntax::   numpy.meshgrid(*xi, copy=True, sparse=False, indexing='xy')

"""

import numpy as np

arr1=np.array([1,2])
arr2=np.array([4,6])

print("Arrray 1")
print(arr1)

print("Array 2")
print(arr2)

combined_array=np.array(np.meshgrid(arr1, arr2)).T.reshape(-1,2)

print("combined Array is :")
print(combined_array)