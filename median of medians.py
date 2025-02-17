def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2] for i in range(0, len(arr), 5)]
    pivot = median_of_medians(medians, len(medians) // 2)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    k_index = len(low)
    if k < k_index:
        return median_of_medians(low, k)
    elif k > k_index:
        return median_of_medians(high, k - k_index - 1)
    else:
        return pivot
arr = [3, 1, 2, 5, 4]
k = 2
print(median_of_medians(arr, k))  
