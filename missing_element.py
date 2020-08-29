a1=[1,2,3,4]
a2=[1,2,3]
def missing_element(a1,a2):
    arr=a1+a2
    result=arr[0]
    for i in range(1,len(arr)):
        result=result^arr[i]
    return result

print(missing_element(a1,a2))