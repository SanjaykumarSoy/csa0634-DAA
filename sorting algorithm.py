def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def find_maximum(arr):
    sorted_arr = bubble_sort(arr)
    return sorted_arr[-1]
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maximum_value = find_maximum(numbers)
print("The maximum value is:", maximum_value)
