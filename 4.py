def length_of_lis(nums):
    if not nums:
        return 0
    
    lis = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    return max(lis)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))
