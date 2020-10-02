# def count(list):
#  if list == []:
#     return 0
#  return 1 + count(list[1:])

def max(list):
 if len(list) == 2:
   return list[0] if list[0] > list[1] else list[1]
 sub_max = max(list[1:])
 return list[0] if list[0] > sub_max else sub_max

print(max([8,2,3,4,5])) 