import sys
sys.setrecursionlimit(10000)
import random
import time
import matplotlib.pyplot as plt

# Median-of-three helper to choose a better pivot
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a = arr[low]
    b = arr[mid]
    c = arr[high]
    # Find median value among a, b, c
    if a <= b <= c or c <= b <= a:
        return mid
    elif b <= a <= c or c <= a <= b:
        return low
    else:
        return high

def partition(arr, low, high):
    pivot_index = median_of_three(arr, low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

# Randomized Quicksort unchanged
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# Performance testing & plotting (same as before)
def measure_time(func, arr):
    start = time.time()
    func(arr, 0, len(arr) - 1)
    return time.time() - start

def performance_analysis():
    sizes = [1000, 5000, 10000, 20000]
    distributions = ["random", "sorted", "reverse"]

    results = {
        "deterministic": {dist: [] for dist in distributions},
        "randomized": {dist: [] for dist in distributions}
    }

    for size in sizes:
        for dist in distributions:
            if dist == "random":
                arr = random.sample(range(size * 10), size)
            elif dist == "sorted":
                arr = list(range(size))
            else:  # reverse
                arr = list(range(size, 0, -1))

            arr_copy1 = arr[:]
            arr_copy2 = arr[:]

            t1 = measure_time(deterministic_quicksort, arr_copy1)
            t2 = measure_time(randomized_quicksort, arr_copy2)

            results["deterministic"][dist].append(t1)
            results["randomized"][dist].append(t2)

            print(f"Size: {size}, Dist: {dist}, Det: {t1:.4f}s, Rand: {t2:.4f}s")

    return sizes, results

def plot_results(sizes, results):
    for dist in results["deterministic"]:
        plt.figure(figsize=(8, 5))
        plt.plot(sizes, results["deterministic"][dist], label="Deterministic", marker="o")
        plt.plot(sizes, results["randomized"][dist], label="Randomized", marker="s")
        plt.title(f"Performance on {dist.capitalize()} Data")
        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    sizes, results = performance_analysis()
    plot_results(sizes, results)
