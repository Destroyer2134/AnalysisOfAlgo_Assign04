import time
import random

# Sorting algorithms as previously defined
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    left_half = arr[left:left + n1]
    right_half = arr[mid + 1:mid + 1 + n2]
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def hybrid_sort(arr, left, right, threshold=10):
    if right - left + 1 <= threshold:
        insertion_sort(arr, left, right)
    else:
        if left < right:
            mid = (left + right) // 2
            hybrid_sort(arr, left, mid, threshold)
            hybrid_sort(arr, mid + 1, right, threshold)
            merge(arr, left, mid, right)

# Experimental comparison of algorithms
array_sizes = [100, 1000, 5000, 10000, 20000]
results = {'Array Size': array_sizes, 'Merge Sort': [], 'Insertion Sort': [], 'Hybrid Sort': []}

for size in array_sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    arr_merge, arr_insertion, arr_hybrid = arr[:], arr[:], arr[:]

    # Measure time for Merge Sort
    start_time = time.time()
    merge_sort(arr_merge, 0, len(arr_merge) - 1)
    results['Merge Sort'].append(time.time() - start_time)

    # Measure time for Insertion Sort
    start_time = time.time()
    insertion_sort(arr_insertion, 0, len(arr_insertion) - 1)
    results['Insertion Sort'].append(time.time() - start_time)

    # Measure time for Hybrid Sort
    start_time = time.time()
    hybrid_sort(arr_hybrid, 0, len(arr_hybrid) - 1, threshold=10)
    results['Hybrid Sort'].append(time.time() - start_time)

# Display the results as a table
results
