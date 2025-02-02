import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def timsort(arr):
    return sorted(arr)

def run_test(size=1000):
    arr = [random.randint(0, 10000) for _ in range(size)]
    
    insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
    merge_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
    timsort_time = timeit.timeit(lambda: timsort(arr.copy()), number=1)
    
    print(f"Array size: {size}")
    print(f"Insertion Sort Time: {insertion_time:.6f} sec")
    print(f"Merge Sort Time: {merge_time:.6f} sec")
    print(f"Timsort Time: {timsort_time:.6f} sec")
    print("-" * 40)

if __name__ == "__main__":
    for size in [1000, 5000, 10000, 50000]:
        run_test(size)
