def meet_in_the_middle(arr, E):
    n = len(arr)
    mid = n // 2
    left_sums = set()
    for i in range(1 << mid):
        current_sum = 0
        for j in range(mid):
            if i & (1 << j):
                current_sum += arr[j]
        left_sums.add(current_sum)
    for i in range(1 << (n - mid)):
        current_sum = 0
        for j in range(n - mid):
            if i & (1 << j):
                current_sum += arr[mid + j]
        if (E - current_sum) in left_sums:
            return True
    return False
arr = [3, 34, 4, 12, 5, 2]
E = 9
print(meet_in_the_middle(arr, E)) 
