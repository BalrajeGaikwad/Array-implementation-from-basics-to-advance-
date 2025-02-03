#numpy.squeeze() function is used when we want to remove single-dimensional entries from the shape of an array.

import numpy as np

arr=([[2,2,2],[2,2,2]])

print("input array ")
print(arr)


out_arr=np.squeeze(arr)

print("output array ")
print(out_arr)