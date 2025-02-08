def selection_sort(arr):
    n = 0
    for i in arr:
        n += 1 
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
array1 = [5, 2, 9, 1, 5, 6]
sorted_random_array = selection_sort(array1)
print("Sorted Random Array:", sorted_random_array)
array2 = [10, 8, 6, 4, 2]
sorted_reverse_array = selection_sort(array2)
print("Sorted Reverse Sorted Array:", sorted_reverse_array)
