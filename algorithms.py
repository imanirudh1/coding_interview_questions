# def count(list):
#  if list == []:
#     return 0
#  return 1 + count(list[1:])

# def max(list):
#  if len(list) == 2:
#    return list[0] if list[0] > list[1] else list[1]
#  sub_max = max(list[1:])
#  return list[0] if list[0] > sub_max else sub_max

# print(max([8,2,3,4,5]))


# a = input()
# n,m,r = list(map(int, a))
# incoming=[]
# outgoing = []
# for i in range(n):
#   b = input()
#   incoming.append(int(b))

# for j in range(m):
#   b = input()
#   outgoing.append(int(b))
# in_sum=0  
# out_sum=0  
# for i in incoming:
#   in_sum+=i
# for j in outgoing:
#   out_sum += j
# out_sum=out_sum-r  
# if in_sum == out_sum:
#   print("Balanced")
# else:
#   print(out_sum-in_sum)  
# graph={}

# graph['start']={}
# graph['start']['a'] = 6
# graph['start']['b'] = 2
# print(graph)

# n = int(input())
# arr = [ [] for i in range(n) ] 
# for i in range(n):
#     j = int(input())
#     l=input()
#     arr[i]=list(map(int,l))
# print(arr)
# count = 0
# length=0
# for i in range(n):
#     for j in range(len(arr[i])):
#         if arr[i][j] == 1:
#             count += 1
#         else:
#             if count >= length:
#                 length = count
#                 count = 0
#     count=0            
#     print(length)
#     length=0            

n=int(input())
strs=[]
for i in range(n):
    a=input()
    strs.append(a)
for j in range(len(strs)):
    even=''
    odd=''
    for k in range(len(strs[j])):
        if k % 2==0:
            even+=strs[j][k]
        else:
            odd+=strs[j][k] 
    print(even,odd)           
