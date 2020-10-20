def unique_path(m, n):
    N = m + n - 2
    r = m - 1
    res=1
    for i in range(1, r + 1):
        res = res * (N - r + i) / i
    return int(res)
    
print(unique_path(3,7))    