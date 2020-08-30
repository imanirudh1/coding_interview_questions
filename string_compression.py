a='aaaAABBccccddddDDD'
def str_comp(a):
    counter=1
    i=1
    r=''
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            counter+=1
        else:
            r=r+a[i-1]+str(counter)
            counter=1
    r=r+a[len(a)-1]+str(counter)    
    return r

print(str_comp(a))               
