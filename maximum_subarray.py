nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4,-9]
def max_subarray(nums):
    total = 0
    max_sum = nums[0]
    for i in range(len(nums)):
        total += nums[i]
        max_sum = max(total, max_sum)
        if total < 0:
            total = 0
    return max_sum

print(max_subarray(nums))
        


