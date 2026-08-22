import numpy as np
import time
 
arr = np.array([1,2,3,4,5,6])
print("1D Array:",arr)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("2D Array:",arr2d)

list = [1,2,3,4,5]    # Size wise multiplication
print("List Multiplication",list*2)

array = np.array(list)      # Element wise multiplication
print("Array Multiplication",array*2)


start = time.time()
py_list = [i*2 for i in range(10000000)]
print("List Operation Time",time.time() - start)


start = time.time()
py_array = np.arange(10000000) * 2
print("Array Operation Time",time.time() - start)

zero = np.zeros([3,4])
print("Zeroes Array \n",zero)

ones = np.ones((3,4))
print("Onces Array \n",ones)

full = np.full((2,3),7)
print("Full \n",full)

random = np.random.random((3,4))
print("Random Matrix: \n",random * 2)

sequence = np.arange(3,31,3)
print(sequence)

tensor = np.array([[[1,2,3],[3,4,5],[6,7,8]],
                     [[9,10,11],[12,13,14],[15,16,17]],
                    [[18,19,20],[21,22,23],[24,25,26]]])
print("Tensor Array: \n",tensor)

Shapes in the Numpy
The Shape is the Property of the Numpy
It is tells the size of the each Dimension of the Array
nums = np.array([[1,2],
                [3,4]])
print("Shape: ",nums.shape)
print("Dimension: ",nums.ndim)
print("Size: ",nums.size)

list = [1,2,9,True,3,4]
print(list)
nums = np.array(list)
print(nums)


Reshaping the Array
nums = np.arange(1,11)
print(nums)
nums = nums.reshape((5,2))
print(nums)


Flattened of the Array
nums = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print("Before Doing Flattened")
print("Original: \n",nums)
print("Shape: ",nums.shape)
print("Dimension: ",nums.ndim)
print("Size: ",nums.size)
nums = nums.flatten()
print("After Flattened")
print("Flattened: ",nums)
print("Shape: ",nums.shape)
print("Dimension: ",nums.ndim)
print("Size: ",nums.size)

print("Transpose of the Matrices")
print(nums.T)
