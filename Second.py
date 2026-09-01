# Create a 4×5 matrix.
# Print shape, dimensions, and size.
# Use reshape().
import numpy as np
 
nums = np.arange(1,21)
print("Original: ",nums)
nums = nums.reshape((4,5))
print("Shape: ",nums.shape)
print("Dimensions: ",nums.ndim)
print("Size: ",nums.size)
print("ReShaped Array: \n",nums)