def countPairs(nums, k):
    count = 0
    freq = {}
    
    for j in range(len(nums)):
        if nums[j] in freq:
            for i in freq[nums[j]]:
                if (i * j) % k == 0:
                    count += 1
        if nums[j] not in freq:
            freq[nums[j]] = []
        freq[nums[j]].append(j)
    
    return count


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
output = countPairs(nums, k)
print(output) 
