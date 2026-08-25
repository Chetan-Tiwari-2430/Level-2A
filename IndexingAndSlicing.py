import numpy as np

# Indexing and Slicing in the 1D Array
# nums = np.array([1,2,3,4,5,6,7,8,9,10])
# print("Basic Slicing: ",nums[2:6])
# print("With Steps Slicing: ",nums[:11:2])
# print("Negative Slicing: ",nums[-1])

# Indexing and Slicing in the 2D Array
nums = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# I need only 5 and 6
# arr = nums[1]
# arr = arr[1:3]
# print(arr)

# print("Specific Element: ",nums[1,2]) # 6
# print("Entire Row: ",nums[1]) # [4,5,6]
# print("Entire Column: ",nums[:,1]) # [2,5,8]
 

# Sorting of the 1 Dimensional Array
# unsorted = np.array([1,7,5,3,5,8,3,2,8,9])
# print("Sorted Array Using the methods: ",np.sort(unsorted))

# Sorting od the 2 Dimensional Array
# unsorted = np.array([[1,3],[3,2],[2,1]])
# print("Sorted Array by the Column: \n",np.sort(unsorted,axis = 0))
# print("Sorted Array by the Row: \n",np.sort(unsorted,axis=1))
# print("Default Sorted: \n",np.sort(unsorted))


# Filtering in the Numpy Array
# Find the Even Numbers

# num = np.arange(1,11)
# even = num % 2 == 0     # We can also give the Expression hear
# print("Even Number: ",num[even])
 
# Merge Two array
a = np.array([1,2,3])
b = np.array([4,5,6])
merge = np.concatenate((a,b))
print("Merge Array: ",merge)



# Check the Two Matrices is comparable or not
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
b = np.array([
    [9,2,9,2],
    [2,3,2,8],
    [3,6,7,7]
])
print("Is comparable: ",a.shape == b.shape)