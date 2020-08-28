arr=[1,3,2,2]
target=4
def pair_sum(arr,target):
    seen=set()
    output=set()
    for i in arr:
        t=target-i
        if t not in seen:
            seen.add(i)
        else:
            output.add((min(i,t),max(i,t)))            
    return len(output)
print(pair_sum(arr,target))            