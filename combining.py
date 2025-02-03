# Combining a one and a two-dimensional NumPy Array

#  Numpy has a function named as numpy.nditer(), which provides this facility.

import numpy as np 

arr1=np.arange(5)
print("one dimensional array")
print(arr1)

arr2=np.arange(10).reshape(2,5)
print("two dimensional array ")
print(arr2)

for a , b in np.nditer([arr1, arr2]):
    print("%d:%d" % (a,b), )