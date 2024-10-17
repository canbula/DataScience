import numpy as np


def replace_center_with_minus_one(d, n, m):
    if d <= 0:
        raise ValueError("d must be greater than 0")

    if n <= 0 or m <= 0:
        raise ValueError("n and m must be positive integers")

    if m > n:
        raise ValueError("m cannot be greater than n")

    # Rastgele d basamaklı sayılarla n x m boyutunda bir numpy array
    array = np.random.randint(0, 10 ** d, size=(n, m))

    # Sadece merkezdeki eleman(lar) -1
    if n % 2 == 1 and m % 2 == 1:  # Hem satır hem sütun tek sayıysa
        center_row = n // 2
        center_col = m // 2
        array[center_row, center_col] = -1
    else:  # Çift boyutlar için, ortadaki 4 eleman -1
        center_row1 = (n // 2) - 1
        center_row2 = n // 2
        center_col1 = (m // 2) - 1
        center_col2 = m // 2
        array[center_row1, center_col1] = -1
        array[center_row1, center_col2] = -1
        array[center_row2, center_col1] = -1
        array[center_row2, center_col2] = -1

    return array


# Test fonksiyonları
def test_replace_center_with_minus_one():
    # Test 1: 3x3 boyutunda, 2 basamaklı sayılarla bir dizi
    d = 2
    n = 5
    m = 5
    array = replace_center_with_minus_one(d, n, m)
    print("\nTest 1: 3x3 Dizi (Orijinal ve Değiştirilmiş Hali):")
    print(array)

    # Test 2: 4x4 boyutunda, 3 basamaklı sayılarla bir dizi
    d = 2
    n = 6
    m = 6
    array = replace_center_with_minus_one(d, n, m)
    print("\nTest 2: 4x4 Dizi (Orijinal ve Değiştirilmiş Hali):")
    print(array)

if __name__ == "__main__":
    test_replace_center_with_minus_one()
