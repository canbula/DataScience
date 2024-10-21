import numpy as np

def replace_center_with_minus_one(d, n, m):
    
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Parametre Hatalı")

    min_sayi = 10**(d - 1) if d > 1 else 0
    max_sayi = 10**d - 1

    array = np.random.randint(min_sayi, max_sayi + 1, size=(n, n))

    remaining_space = n - m
    start_index = remaining_space // 2
    end_index = start_index + m

    array[start_index:end_index, start_index:end_index] = -1

    return array

try:
    d = 4
    n = 6
    m = 2
    result = replace_center_with_minus_one(d, n, m)
    print(result)
except ValueError as e:
    print(f"ValueError: {e}")
