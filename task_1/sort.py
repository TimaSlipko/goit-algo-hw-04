import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def generate_data(size, data_type):
    if data_type == 'random':
        return [random.randint(0, 10000) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(size))
    elif data_type == 'reversed':
        return list(range(size, 0, -1))

def measure(sort_func, data, runs):
    return timeit.timeit(lambda: sort_func(data.copy()), number=runs) / runs

def main():
    sizes = [100, 500, 1000, 5000]
    data_types = ['random', 'sorted', 'reversed']
    results = {}
    
    for dtype in data_types:
        results[dtype] = {}
        for size in sizes:
            data = generate_data(size, dtype)
            results[dtype][size] = {
                'insertion': measure(insertion_sort, data, 10),
                'merge': measure(merge_sort, data, 10),
                'timsort': measure(sorted, data, 10)
            }
    
    for dtype in data_types:
        print(f"\n{dtype}:")
        for size in sizes:
            r = results[dtype][size]
            print(f"  {size}: insertion={r['insertion']:.6f}, merge={r['merge']:.6f}, timsort={r['timsort']:.6f}")

if __name__ == "__main__":
    main()