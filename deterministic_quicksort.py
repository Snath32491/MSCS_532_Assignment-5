def partition(arr, low, high):
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

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    deterministic_quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
