def partition(array, low, high):
    pivot = array[low]
    start = low + 1
    end = high
    while True:
        while start <= end and array[end] >= pivot:
            end = end - 1
        while start <= end and array[start] <= pivot:
            start = start + 1
        if start <= end:
            array[start], array[end] = array[end], array[start]
        else:
            break
    array[low], array[end] = array[end], array[low]
    return end

def quick_sort(array, start, end):
    if start < end:
        idx = partition(array, start, end)
        quick_sort(array, start, idx-1)
        quick_sort(array, idx+1, end)

def print_arr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

arr1 = [7, 6, 10, 5, 9, 2, 1, 15, 7]
quick_sort(arr1, 0, len(arr1)-1)
print_arr(arr1, len(arr1))
