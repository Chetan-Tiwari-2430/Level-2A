import time
import numpy as np


start = time.perf_counter()
list = [10,10,203,46,54,645,6,6,4,6,45,6,57,45,436,34,634,6,346,437,45,7,54]
for i in list:
    i = i + 1
end = time.perf_counter()
s = end - start
print("List Takes Time: ",s)

start = time.perf_counter()
nums = np.array([10,10,203,46,54,645,6,6,4,6,45,6,57,45,436,34,634,6,346,437,45,7,54])
for i in nums:
    i = i+1
end = time.perf_counter()
print("Arrays Takes Time: ",end - start)

