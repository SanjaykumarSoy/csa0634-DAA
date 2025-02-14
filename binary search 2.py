def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = left + (right - left) // 2
        comparisons += 1

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons

# Test the binary search function
array = [5, 10, 15, 20, 25, 30, 35, 40, 45]
target_element = 20
index, comparison_count = binary_search(array, target_element)

print(f"Index of element {target_element}: {index}")
print(f"Number of comparisons made: {comparison_count}")
