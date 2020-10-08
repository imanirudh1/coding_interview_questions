a = [3,3,2,4,1]

def fun(a):
    count = 0
    for i in range(len(a)):
        largest = a[0]
        seclargest = 0
        for j in range(1, len(a)):
            if a[j] >= largest:
                largest = a[j]
        print(largest)
        for k in range(len(a)):
            if a[k] < largest and a[k] != largest:
                if a[k]>=seclargest:
                    seclargest = a[k]
        print(seclargest)        
        diff = largest - seclargest
        print(diff)
        for l in range(len(a)):
            if a[l] == largest:
                a[l] = a[l] - diff
                count=count+1
        print(a)        
        for i in range(1,len(a)):
            if a[i]==a[i-1]:
                if i == len(a) - 1:
                    return count
            else:
                break                       
print(fun(a))        