def find_max_min(arr):
    max_value = max(arr)
    min_value = min(arr)
    return max_value, min_value
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maximum, minimum = find_max_min(array)
print("Maximum value:", maximum)
print("Minimum value:", minimum)
