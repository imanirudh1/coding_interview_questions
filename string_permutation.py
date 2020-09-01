a='abc'
def permutation(a):
    out=[]
    if len(a)==1:
        out=[a]
        print(out)
    for i,let in enumerate(a):
        for perm in permutation(a[:i]+a[i+1:]):
            print('perm is ',perm)
            out+=[let+perm]
            print(out)
    return out        

print(permutation(a))