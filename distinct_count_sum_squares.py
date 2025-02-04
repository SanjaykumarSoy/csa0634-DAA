def distinct_count_sum_squares(nums):
    n = len(nums)
    total_sum = 0
    
    for i in range(n):
        distinct_values = set()
        for j in range(i, n):
            distinct_values.add(nums[j])
            total_sum += len(distinct_values) ** 2
            
    return total_sum


nums = [1, 2, 1]
output = distinct_count_sum_squares(nums)
print(output)
