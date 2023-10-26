import numpy as np


# non-vectorized
list_1 = [1, 2, 3, 4, 5]
list_2 = [10, 20, 30, 40, 50]

result = list_1 + list_2
print(f"result: {result}")

result = []
for i in range(len(list_1)):
    result.append(list_1[i] + list_2[i])

print(f"result: {result}")

# vectorized
array_1 = np.array([1, 2, 3, 4, 5])
array_2 = np.array([10, 20, 30, 40, 50])
result = array_1 + array_2
print(f"result: {result}")


# broadcasting
new_list = 2 * list_1
print(f"new_list: {new_list}")

new_array = 2 * array_1
print(f"new_array: {new_array}")
