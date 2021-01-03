arr = [1, 1, 2, 3, 3, 3, 3, 3, 4]

def remove_dub(arr):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    i+=1
    return i            
        
print(remove_dub(arr))        