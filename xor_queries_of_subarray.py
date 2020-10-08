# arr = [1, 3, 4, 8]
# queries = [[0,1],[1,2],[0,3],[3,3]]
# result=[]
# for i in range(len(queries)):
#     li = queries[i][0]
#     ri = queries[i][1]
#     xor=0
#     if li == ri:
#         result.append(arr[li])
#     else:
#         xor=arr[li]
#         for j in range(li, ri):
#             xor =xor ^ arr[j+1] 
#             print('xor : ',xor)
#         result.append(xor)        
#     print('-------')        
# print(result)

arr = [4, 8, 2, 10]
queries = [[2,3],[1,3],[0,0],[2,3]]
def xorQueries(arr, queries):
    xors = [arr[0]]
    n = len(arr)
    for i in range(1, n):
        xors.append(xors[-1] ^ arr[i])
    print('xor ',xors)    
    res = []
    for l,r in queries:
        temp = xors[r]
        if l != 0:
            temp ^= xors[l - 1]
        res.append(temp)
    return res
print(xorQueries(arr,queries))
