const grid_traversal=(m,n,memo={})=>{
var key = m+","+n
if(key in memo) return memo[key]
if(m==0 || n==0) return 0
if(m>0 && n >0) return 1
memo[key]=grid_traversal(m-1,n,memo)+grid_traversal(m,n-1,memo)
return memo[key]

}
