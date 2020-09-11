def insertion_sort(arr):
    for n in range(1,len(arr)):
        for j in range(n,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
    return arr

a=[17,26,54,77,93,31,44,55]
print(insertion_sort(a))