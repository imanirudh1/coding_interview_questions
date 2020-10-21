def two_sum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return [dic[nums[i]], i]
        else:
            dic[target-nums[i]]=i    
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums,target))