a=[1,2,-1,3,4,10,10,-10,-10,-1,40-65]
def large_cont_sum(a):
    current_sum=max_value=a[0]
    for i in a[1:]:
        current_sum=max(current_sum+i,i)
        max_value=max(current_sum,max_value)
    return max_value

print(large_cont_sum(a))