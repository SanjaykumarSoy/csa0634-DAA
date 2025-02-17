from itertools import combinations
def meet_in_the_middle(arr, target):
    n = len(arr)
    mid = n // 2
    left_part = arr[:mid]
    right_part = arr[mid:]
    left_sums = {sum(comb) for r in range(len(left_part) + 1) for comb in combinations(left_part, r)}
    right_sums = {sum(comb) for r in range(len(right_part) + 1) for comb in combinations(right_part, r)}
    closest_sum = float('inf')
    for left_sum in left_sums:
        for right_sum in right_sums:
            current_sum = left_sum + right_sum
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
    return closest_sum
arr = [1, 2, 3, 4, 5]
target = 10
result = meet_in_the_middle(arr, target)
print("Closest sum to target:", result)
