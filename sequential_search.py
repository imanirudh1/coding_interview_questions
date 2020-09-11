arr=[1,2,3,4,5]
def seq_search(arr,ele):
    pos=0
    found=False
   
    while pos < len(arr) and not found :
        if arr[pos] == ele:
            return True
        else:
            pos += 1
    return found        

print(seq_search(arr,6))
# input array must be sorted

# def seq_search(arr,ele):
#     pos=0
#     found=False
#     stopped=False
#     while pos < len(arr) and not found and not stopped:
#         if arr[pos] == ele:
#             return True
#         else:
#             if arr[pos]>ele:
#                 stopped=True
#             else:
#                 pos += 1
#     return found        
