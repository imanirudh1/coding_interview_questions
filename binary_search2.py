def bin_srch(arr,key):
    l=0
    u=len(arr)-1
    found=False
    while l<=u and not found:
        mid=(l+u)//2
        if arr[mid] == key:
            return 'Element Present in the index pos:' + str(mid)
        else:
            if key > arr[mid]:
                l=mid+1
            else:
                u=mid-1
    return 'Key not found'
arr=[1,2,3,4,5,6]
print(bin_srch(arr,5))  
'''
Method 2
'''
# def rec_bin(arr,ele):
#     if len(arr)==0:
#         return False
#     else:
#         mid=len(arr)//2
#         if arr[mid]==ele:
#             return True
#         else:
#             if ele > arr[mid]:
#                 return rec_bin(arr[mid+1:],ele)
#             else:
#                 return rec_bin(arr[:mid])         