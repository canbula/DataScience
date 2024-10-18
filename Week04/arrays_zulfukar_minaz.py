import random
import numpy as np


def replace_center_with_minus_one(d: int, n: int, m: int) -> [[], []]:
    if m > n or d <= 0 or m < 0 or n < 0:
        raise ValueError
    else:
        arr = np.zeros((n, n), dtype=int)
        if n == m:
            arr[:, :] = -1
            return arr
        else:
            for i in range(n):
                for j in range(n):
                    r = random.randint(10**(d-1), (10**d)-1)
                    arr[i, j] = r
            arr[((n - m) // 2):((n + m) // 2), ((n - m) // 2):((n + m) // 2)] = -1
    return arr
