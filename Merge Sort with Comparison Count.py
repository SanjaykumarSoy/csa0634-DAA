

def merge_sort(arr, count):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, count)
        merge_sort(R, count)

        i = j = k = 0

        while i < len(L) and j < len(R):
            count[0] += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [12, 4, 78, 23, 45, 67, 89, 1]
comparison_count = [0]
merge_sort(arr, comparison_count)

print("Sorted array:", arr)
print("Number of comparisons:", comparison_count[0])
