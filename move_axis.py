#  numpy.moveaxis() function | Python

import numpy as np

arr=np.array([[1,2,3,4]])

new_arr=np.moveaxis(arr, -1,0)

print(new_arr)



# Python program explaining 
# numpy.moveaxis() function 

# importing numpy as geek 
import numpy as geek 

arr = geek.zeros((1, 2, 3, 4)) 

gfg = geek.moveaxis(arr, 0, -1).shape 

print (gfg) 
