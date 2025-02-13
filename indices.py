def count_indices(nums1, nums2):
    answer1 = sum(1 for i in nums1 if i in nums2)
    answer2 = sum(1 for i in nums2 if i in nums1)
    return [answer1, answer2]

# Example usage
nums1 = [2, 3, 2]
nums2 = [1, 2]
output = count_indices(nums1, nums2)
print(output)  # Output: [2, 1]
