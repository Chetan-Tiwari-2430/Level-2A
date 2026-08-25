# Extract first 10, last 5, alternate elements.
import numpy as np
nums = np.arange(1,51)
print("Original Array: ",nums)
# First 10 Element
ten_elements = nums[:10]
print("First Ten elements: ",ten_elements)
# Last 5 Elements
five_last_elements = nums[-5:]
print("Last Five Elements: ",five_last_elements)
# Alternate Elements
print("Alternate Elements: ",nums[::2])