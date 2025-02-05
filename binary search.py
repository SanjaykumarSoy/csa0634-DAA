def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return f"Element {x} is found at position {mid}"
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return "Element not found"
X = [3, 4, 6, -9, 10, 8, 9, 30]
X.sort() 
key = 10
print(binary_search(X, key))
