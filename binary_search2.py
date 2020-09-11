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
