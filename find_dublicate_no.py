nums = [1, 3, 4, 2, 2, 1]
def find_dublicate(nums):
    if len(nums) > 1:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow
    return -1        
print(find_dublicate(nums))    