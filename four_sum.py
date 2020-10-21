def fourSum(nums, target):
n = len(nums)
    if n <= 3:
        return []

    nums.sort()
    i = 0
    L = []
    store = {}
    
    while i < n:
        if target < 4*nums[i] or target > 4*nums[n-1]:  # **MISSING THIS**
            break
        
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue
        j = i+1
        while j < n:
            target3 = target - nums[i]
            if target3 < 3*nums[j] or target3 > 3*nums[n-1]:  # **MISSING THIS**
                break
            if j > i+1 and nums[j] == nums[j-1]:
                j += 1
                continue
            
            twoSum(nums[j+1:], nums[i], nums[j], target - nums[i] - nums[j], L, store)
            j += 1
        i += 1

    return L