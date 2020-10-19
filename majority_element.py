def majorityElement( nums):
    count=0
    ele=0
    for i in nums:
        if count==0:
            ele=i
        if i==ele:
            count+=1
        else:
            count-=1
    return ele
nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))    