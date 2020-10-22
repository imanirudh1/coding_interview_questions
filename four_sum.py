# def fourSum(nums, target):
#     n = len(nums)
#     if n <= 3:
#         return []

#     nums.sort()
#     i = 0
#     L = []
#     store = {}
    
#     while i < n:
#         if target < 4*nums[i] or target > 4*nums[n-1]:  # **MISSING THIS**
#             break
        
#         if i > 0 and nums[i] == nums[i-1]:
#             i += 1
#             continue
#         j = i+1
#         while j < n:
#             target3 = target - nums[i]
#             if target3 < 3*nums[j] or target3 > 3*nums[n-1]:  # **MISSING THIS**
#                 break
#             if j > i+1 and nums[j] == nums[j-1]:
#                 j += 1
#                 continue
            
#             twoSum(nums[j+1:], nums[i], nums[j], target - nums[i] - nums[j], L, store)
#             j += 1
#         i += 1

#     return L


#     def fourSum(self, n: List[int], t: int) -> List[List[int]]:
#     	if not n: return []
#     	n.sort()
#     	L, N, S, M = len(n), {j:i for i,j in enumerate(n)}, set(), n[-1]
#     	for i in range(L-3):
#     		a = n[i]
#     		if a + 3*M < t: continue
#     		if 4*a > t: break
#     		for j in range(i+1,L-2):
#     			b = n[j]
#     			if a + b + 2*M < t: continue
#     			if a + 3*b > t: break
#     			for k in range(j+1,L-1):
#     				c = n[k]
#     				d = t-(a+b+c)
#     				if d > M: continue
#     				if d < c: break
#     				if d in N and N[d] > k: S.add((a,b,c,d))
#     	return S


# def fourSum(nums, target):       
#     nums.sort()
#     length=len(nums)    
#     if (length<4):
#         return []    
#     maxnum=nums[-1]             
#     d={}    
#     for i,num in enumerate(nums):
#         d[num]=i
#     ans=set()     
#     for i in range(length-3):    
#         i_=nums[i]
#         if (4*i_>target):
#             break
#         if (i_+3*maxnum<target):
#             continue            
#         for j in range(i+1,length-2):                
#             j_=nums[j]
#             if (i_+3*j_>target):
#                 break
#             if (i_+j_+2*maxnum<target):
#                 continue                
#             for k in range(j+1,length-1):                    
#                 k_=nums[k]
#                 missing=target-i_-j_-k_                    
#                 if (missing<k_):
#                     break
#                 if (missing in d and d[missing]>k):
#                     ans.add((i_,j_,k_,missing))        
#     return ans        
nums = [1, 0, -1, 0, -2, 2]
target = 0
def fourSum(nums, target):
    n = len(nums)
    res=[]
    if n==None or n < 4:
        return res
    nums = sorted(nums)
    for i in range(n):

        for j in range(i + 1, n):
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    l = []
                    l.append(nums[i])
                    l.append(nums[j])
                    l.append(nums[left])
                    l.append(nums[right])
                    res.append(l)
                    leftVal = nums[left]
                    while left < n and leftVal == nums[left]:
                        left += 1
                    rightVal = nums[right]
                    while right > left and rightVal == nums[right]:
                        right -= 1
                else:
                    if total < target:
                        left += 1
                    else:
                        right-=1    
            while j + 1 < n and nums[j] == nums[j + 1]:
                j += 1
        while i + 1 < n and nums[i] == nums[i + 1]:
            i += 1
    return res        
               
print(fourSum(nums,target))