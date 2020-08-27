n=int(input())
z=[]
z=list(map(int,input().split()))
answer = z[0]
for i in z[1:]:
    answer = (answer*i)%(10**9 + 7)
print(answer)