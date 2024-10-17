import numpy as np


def replace_center_with_minus_one(d, n, m):
    if d <= 0 or n <= 0 or m <= 0:
        raise ValueError("Invalid input parameters.")

    # n x m boyutunda rastgele bir dizi oluştur
    arr = np.random.randint(0, 10 ** d, size=(n, m))
    print(f"Orijinal Dizi (n={n}, m={m}):\n", arr)

    # Merkezi belirle ve sadece merkezi -1 yap
    if n % 2 == 1 and m % 2 == 1:
        # Tek boyutlar
        center_row = n // 2
        center_col = m // 2
        arr[center_row, center_col] = -1
    elif n % 2 == 0 and m % 2 == 0:
        # Çift boyutlar
        center_row1 = n // 2 - 1
        center_row2 = n // 2
        center_col1 = m // 2 - 1
        center_col2 = m // 2
        arr[center_row1:center_row2 + 1, center_col1:center_col2 + 1] = -1
    elif n > m:
        # n > m olduğunda
        center_row_start = (n - m) // 2
        center_row_end = center_row_start + m
        arr[center_row_start:center_row_end, :] = -1
    elif m > n:
        # m > n olduğunda
        center_col_start = (m - n) // 2
        center_col_end = center_col_start + n
        arr[:, center_col_start:center_col_end] = -1

    print(f"Değiştirilen Dizi:\n", arr)
    return arr


# Test Fonksiyonları
def test_replace_center_with_minus_one():
    # Test 1: 5x5
    d = 2
    n = 5
    m = 5
    print("\nTest 1: 5x5 dizi")
    array = replace_center_with_minus_one(d, n, m)

    # Test 2: 4x4
    d = 3
    n = 4
    m = 4
    print("\nTest 2: 4x4 dizi")
    array = replace_center_with_minus_one(d, n, m)

    # Test 3: 5x3
    d = 2
    n = 5
    m = 3
    print("\nTest 3: 5x3 dizi")
    array = replace_center_with_minus_one(d, n, m)

    # Test 4: 3x5
    d = 2
    n = 3
    m = 5
    print("\nTest 4: 3x5 dizi")
    array = replace_center_with_minus_one(d, n, m)

if __name__ == "__main__":
    test_replace_center_with_minus_one()
