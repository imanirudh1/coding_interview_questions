grid=[[1,3,1],[1,5,1],[4,2,1]]
row=3
col=3
top=0
left=0

min_path_sum=[[0 for j in range(col)] for i in range(row)]
parent=[[(None,None) for j in range(col)] for i in range(row)]
for r in range(row):
    for c in range(col):
        if r==0 and c==0 :
            min_path_sum[r][c]=grid[0][0]
        else:
            top = min_path_sum[r-1][c] if r!=0 else float("inf")

            left = min_path_sum[r][c-1] if c!=0 else float("inf")
            if top<left:
                parent[r][c]=(r-1,c)
            else:
                parent[r][c]=(r,c-1)
            min_path_sum[r][c]=min(top,left)+grid[r][c]             
print(min_path_sum[row-1][col-1])
# for i in range(3):
#     for j in range(3):
#         top=grid[i][j] if j!=0 else float("inf")
#         print(top)        