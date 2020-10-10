ar1 = [10, 27, 38, 43, 82]
ar2 = [3, 9]
n = len(ar1)
m = len(ar2)
def find_gap(gap):
    if (gap <= 1):
        return 0
    return (gap//2) + (gap%2)    

def merge(a1, a2, n, m):
    gap = n + m
    gap = find_gap(gap)
    while gap > 0:
        i = 0
        while gap + i < n:
            if a1[i] > a1[gap + i]:
                a1[i], a1[gap + i] = a1[gap + i], a1[i]
            i += 1
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if a1[i] > a2[j]:
                a1[i], a2[j] = a2[j], a1[i]
            i += 1
            j += 1
        if j < m:
            j=0
            while j + gap < m:
                if a2[j] > a2[j + gap]:
                    a2[j], a2[j + gap] = a2[j + gap], a2[j]
                j += 1
        gap=find_gap(gap)     
merge(ar1,ar2,n,m)
print(ar1)                    
print(ar2)                    
                
                         