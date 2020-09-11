def selec_sort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr            

arr=[5,3,2,1,0]
print(selec_sort(arr))