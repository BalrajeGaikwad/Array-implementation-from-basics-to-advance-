# Check whether a Numpy array contains a specified row


# importing package 
import numpy 

# create numpy array 
arr = numpy.array([[1, 2, 3, 4, 5], 
				[6, 7, 8, 9, 10], 
				[11, 12, 13, 14, 15], 
				[16, 17, 18, 19, 20] 
				]) 

# view array 
print(arr) 

# check for some lists 
print([1, 2, 3, 4, 5] in arr.tolist()) 
print([16, 17, 20, 19, 18] in arr.tolist()) 
print([3, 2, 5, -4, 5] in arr.tolist()) 
print([11, 12, 13, 14, 15] in arr.tolist()) 
