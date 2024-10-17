import random

def replace_center_with_minus_one(d, n, m):
    # Rastgele d basamaklı sayılarla n x m boyutunda bir dizi
    array = [[random.randint(0, 10 ** d - 1) for _ in range(m)] for _ in range(n)]

    if n % 2 == 1 and m % 2 == 1:  # Tek boyut
        center_row = n // 2
        center_col = m // 2
        array[center_row][center_col] = -1
    else:  # Çift boyut
        center_row1 = (n // 2) - 1
        center_row2 = n // 2
        center_col1 = (m // 2) - 1
        center_col2 = m // 2
        array[center_row1][center_col1] = -1
        array[center_row1][center_col2] = -1
        array[center_row2][center_col1] = -1
        array[center_row2][center_col2] = -1
    return array


# Test fonksiyon
if __name__ == "__main__":
    # Test 1: 2 basamaklı, 3x3 boyutunda bir dizi
    d = 2
    n = 3
    m = 3
    print("Test 1: 3x3 dizi:")
    result = replace_center_with_minus_one(d, n, m)
    for row in result:
        print(row)

    # Test 2: 3 basamaklı, 4x4 boyutunda bir dizi
    d = 3
    n = 4
    m = 4
    print("\nTest 2: 4x4 dizi:")
    result = replace_center_with_minus_one(d, n, m)
    for row in result:
        print(row)
