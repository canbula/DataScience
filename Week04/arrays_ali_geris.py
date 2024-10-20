import numpy as np


def replace_center_with_minus_one(d, n, m):
    if d <= 0 or n <= 0 or m <= 0:
        raise ValueError("Invalid input parameters.")
    if m > n:
        raise ValueError("m cannot be greater than n")

    low = 10 ** (d - 1)  # d-1 basamağından başlayarak low değeri
    high = 10 ** d  # d basamağına göre high değeri

    # Geçerli bir aralık mı?
    if low >= high:
        raise ValueError(f"Invalid range for random generation: low={low}, high={high}")

    arr = np.random.randint(low, high, size=(n, n))

    start = (n - m) // 2
    end = start + m
    arr[start:end, start:end] = -1

    return arr


# Test
def test_replace_center_with_minus_one():
    print("\nTest 1: 5x5 dizi ve merkez 3x3 -1 yapılmış olmalı")
    d = 2
    n = 5
    m = 3

    array = replace_center_with_minus_one(d, n, m)

    print("Oluşturulan Dizi:")
    print(array)

    center = array[1:4, 1:4]
    assert np.all(center == -1), "Merkez -1 ile doldurulmalı!"
    print("Merkez -1 yapıldı, test başarılı.")

if __name__ == "__main__":
    test_replace_center_with_minus_one()
