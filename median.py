def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2] for i in range(0, len(arr), 5)]
    pivot = median_of_medians(medians, len(medians) // 2)
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + arr.count(pivot):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - arr.count(pivot))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k=6
print(median_of_medians(arr,k))
