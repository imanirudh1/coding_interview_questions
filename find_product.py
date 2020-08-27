n=int(input())
z=[]
for i in range(0,n):
    a=int(input())
    z.append(a)
answer = z[0]
for i in z[1:]:
    answer = (answer*i)%(10**9 + 7)
    print(answer)