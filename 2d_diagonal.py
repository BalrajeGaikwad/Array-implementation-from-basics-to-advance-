# How to get all 2D diagonals of a 3D NumPy array?
"""
program for getting all 2D diagonals of a 3D NumPy array. 
So, for this we are using ----- numpy.diagonal() ------ function of NumPy library. 
This function return specified diagonals from an n-dimensional array. 


Syntax: numpy.diagonal(a, axis1, axis2)
Parameters: 


a: represents array from which diagonals has to be taken 
axis1: represents first axis to be taken for 2-d subarray 
axis2: represents second axis to be taken for 2-d subarray 

Return: array of diagonal elements.

"""

import numpy as np 

arr=np.arange(3 * 4 * 4).reshape(3,4,4)
print("original array")
print(arr)

diag_arr=np.diagonal(arr,axis1=1, axis2=2)

print("diag_arr" )
print(diag_arr)