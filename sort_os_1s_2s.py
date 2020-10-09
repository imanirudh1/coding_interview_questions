nums=[0,2,0,1,0,1,1,2]
def sortColors(nums):      
    low=0
    mid=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==1:
            mid+=1
        elif nums[mid]==2:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
        else:
            nums[mid],nums[low]=nums[low], nums[mid]
            low+=1
            mid += 1
    return nums    
print(sortColors(nums))
       