# Generate 100 random integers (1–100).
# Display mean and maximum value.
import numpy as np
nums = np.random.randint(1,100,100)
print("Minimum in The Array: ",min(nums))
print("Maximum in The Array: ",max(nums))
print("Random Array \t",nums)