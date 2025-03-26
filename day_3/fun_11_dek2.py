import time
import numpy as np


# pip install numpy

def measure_time(func):
    def wrappper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrappper


@measure_time
def my_wait():
    time.sleep(3)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_sum_sum():
    total = sum(range(15_000_000))
    print("Sum is:", total)


@measure_time
def sum_np():
    total = np.sum(np.arange(15_000_000))
    print("Sum is:", total)


print("----Start----")
my_wait()  # Czas wykonania funkcji my_wait: 3.00282621383667
my_for_sum()  # Czas wykonania funkcji my_for_sum: 1.0860099792480469
my_sum_sum()  # Czas wykonania funkcji my_sum_sum: 0.37380480766296387
sum_np()  # Czas wykonania funkcji sum_np: 0.15379905700683594
