import numpy as np


def replace_center_with_minus_one(d, n, m):
    if d <= 0 or n <= 0 or m <= 0:
        raise ValueError("Invalid input parameters.")

    if m > n:
        raise ValueError("m cannot be greater than n")

    # n x n boyutunda rastgele bir dizi oluştur
    arr = np.random.randint(0, 10 ** d, size=(n, n))
    print(f"Orijinal Dizi (n={n}, m={m}):\n", arr)

    if n == m:
        if n % 2 == 1:
            center_row = n // 2
            center_col = m // 2
            arr[center_row, center_col] = -1
        else:
            center_row1 = n // 2 - 1
            center_row2 = n // 2
            center_col1 = m // 2 - 1
            center_col2 = m // 2
            arr[center_row1:center_row2 + 1, center_col1:center_col2 + 1] = -1

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


if __name__ == "__main__":
    test_replace_center_with_minus_one()
