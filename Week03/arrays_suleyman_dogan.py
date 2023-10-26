import numpy as np

def replace_center_with_minus_one(d, n, m):
    # n is the size of the array
    # m is the size of the center
    # d is the number of digits of the maximum value
    if n < 0:
        return "Expected an error for negative n"  # n < 0
    if m < 0:
        return "Expected an error for negative m" # m < 0
    if m > n:
        return "Expected an error when m > n" # m > n
    if d <= 0:
        return "Expected an error when d <= 0" # d <= 0

    # Minimum and maximum values for the random array
    min_value = 10 ** (d - 1)
    max_value = (10 ** d) - 1
    
    #Numpy create random array with size n*n and values between min_value and max_value
    random_array = np.random.randint(min_value, max_value, (n, n))
    center_size = min(m, n)
    
    start_index = (n - center_size) // 2
    end_index = start_index + center_size
    random_array[start_index:end_index, start_index:end_index] = -1
    
    return random_array

