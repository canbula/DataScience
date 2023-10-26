import numpy as np


array_0 = np.array([True, False, True, True, True])
array_1 = np.array([True, False, True, True, 1])
array_2 = np.array([1, 2, 3, 4, 5])
array_3 = np.array([1, 2, 3, 4, 5.0])
array_4 = np.array([1, 2, 3, 4, 5.0], dtype=np.int64)
array_5 = np.array([1, 2, 3, 4, 5.1], dtype=np.int64)
array_6 = np.array([1, 2, 3, 4, 5.9], dtype=np.int64)
array_7 = np.array([1, 2, 3, 4, "5"])
array_8 = np.array([1, 2, 3, 4, "5"], dtype=np.int32)
array_9 = np.array([1, 2, 3, 4, 5j])

for i in range(10):
    print(
        f"array_{i}: {eval(f'array_{i}')} {eval(f'array_{i}').dtype} {eval(f'array_{i}').itemsize}"
    )
