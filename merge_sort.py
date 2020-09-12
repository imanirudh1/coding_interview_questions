def merge_sort(arr):
    if len(arr) > 1:
        mid=len(arr)//2
        lefthalf=arr[:mid]
        righthalf=arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf): 
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i+=1
            else:
                arr[k]=righthalf[j]
                j+=1
            k+=1
        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            k+=1
            i+=1
        while j < len(righthalf):
            arr[k]=righthalf[j]
            j+=1
            k+=1
    print('Merging ',arr)        

arr = [11,2,5,4,7,6,8,1,23]
merge_sort(arr)
print(arr)

'''
Output:

Merging  [11]
Merging  [2]
Merging  [2, 11]
Merging  [5]
Merging  [4]
Merging  [4, 5]
Merging  [2, 4, 5, 11]
Merging  [7]
Merging  [6]
Merging  [6, 7]
Merging  [8]
Merging  [1]
Merging  [23]
Merging  [1, 23]
Merging  [1, 8, 23]
Merging  [1, 6, 7, 8, 23]
Merging  [1, 2, 4, 5, 6, 7, 8, 11, 23]
[1, 2, 4, 5, 6, 7, 8, 11, 23]
'''