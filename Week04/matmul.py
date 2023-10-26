from time import perf_counter
from memory_profiler import memory_usage
import numpy as np
import random


def matrix_multiply_without_numpy(a, b):
    result = [[0 for j in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


def matrix_multiply_with_numpy(a, b):
    return np.dot(a, b)


if __name__ == "__main__":
    SIZE = 20
    a = [[random.randint(10, 99) for j in range(SIZE)] for i in range(SIZE)]
    b = [[random.randint(10, 99) for j in range(SIZE)] for i in range(SIZE)]
    a_np = np.array(a)
    b_np = np.array(b)

    start_traditional = perf_counter()
    memory_traditional = memory_usage((matrix_multiply_without_numpy, (a, b)))
    end_traditional = perf_counter()

    start_numpy = perf_counter()
    memory_numpy = memory_usage((matrix_multiply_with_numpy, (a_np, b_np)))
    end_numpy = perf_counter()

    print(f"            |   Time(s)  | Memory (MB)")
    print(f"------------|------------|------------")
    print(
        f"Python      |{end_traditional - start_traditional:12.4f}|{max(memory_traditional) - min(memory_traditional):12.4f}"
    )
    print(
        f"NumPy       |{end_numpy - start_numpy:12.4f}|{max(memory_numpy) - min(memory_numpy):12.4f}"
    )
