#Reverse a numpy array

import numpy as np
array=np.array([1,2,3,4,5,6])

rev=np.flip(array)

print("final array", str (rev))

"""
1) Using flip() function to Reverse a Numpy array
The numpy.flip() function reverses the order of array elements along the specified axis, preserving the shape of the array.

2) Possible also by using the slicing operator 

"""