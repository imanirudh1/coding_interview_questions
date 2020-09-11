def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                arr[k],arr[k+1]=arr[k+1],arr[k]
    return arr            

a=[11,88,7,4,4,4,0]
print(bubble_sort(a))