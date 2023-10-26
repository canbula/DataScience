import numpy as np

def replace_center_with_minus_one(d, n, m):
    if m > n:
        raise ValueError("m cannot be greater than n.")
    if d <= 0:
        raise ValueError("d must be greater than 0.")
    if n < 0:
        raise ValueError("n cannot be negative")
    if m < 0:
        raise ValueError("m cannot be negative")

    start = (n - m) // 2
    end = start + m

    array = np.random.randint(0, (10**d), size=(n, n))
    
    array[start:end, start:end] = -1
    
    return array
