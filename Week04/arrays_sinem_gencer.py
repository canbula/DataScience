import numpy as np

def replace_center_with_minus_one(d, n, m):
    """
    Check if inputs are valid
    """
    if d <= 0 or n <= 0 or m <= 0:
        raise ValueError("Parameters d, n, and m must be positive integers.")
    if m > n:
        raise ValueError("Center size m cannot be greater than array size n.")
    """
    Create array of nxn size filled with random values using d
    """
    outer_min = 10 ** (d - 1)
    outer_max = 10 ** d
    arr = np.random.randint(outer_min, outer_max, size=(n, n))

    """
    Get indices for center according to m value given
    """
    start = (n - m) // 2
    end = start + m

    """
    Fill mxm array in the center with -1
    """
    arr[start:end, start:end] = -1

    return arr
