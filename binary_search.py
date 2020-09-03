pos=0
def search(arr,n):
    l=0
    u=len(arr)-1
   
    while l <= u:
        mid=(l+u)//2
        if arr[mid]==n:
            global pos
            pos=mid
            return True
        else: 
            if arr[mid]<n:
                l=mid+1
            else:
                u=mid-1 
    return False               
arr=[4,7,8,12,45,93]
n=93
if search(arr,n):
    print('found at index ',pos)
else:
    print("not found")    
                