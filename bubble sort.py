def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Time Complexity Analysis:
# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)
