import numpy as np
import random

def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m must be less than or equal to n")
    if d <= 0:
        raise ValueError("d must be greater than 0")
    if n <= 0 or m <= 0:
        raise ValueError("n and m must be positive")

    arr = random.randint(10**(d-1), (10**d)-1)

    if m == n:
        arr.fill(-1)
    else:
        start_idx = (n - m) // 2
        end_idx = start_idx + m
        arr[start_idx:end_idx, start_idx:end_idx] = -1

    return arr
