import numpy as np

def replace_center_with_minus_one(d, n, m):
    if d <= 0 or m > n or n <= 0 or m <= 0:
        raise ValueError("Invalid input parameters.")

    # Rastgele sayılar 1 ile 10^d arasında olmalı
    arr = np.random.randint(1, 10**d, size=(n, n))
    center_start = (n - m) // 2
    center_end = center_start + m
    arr[center_start:center_end, center_start:center_end] = -1

    return arr
