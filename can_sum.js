const cansum=(target,nums,memo={})=>{
if(target in memo) return memo[target]
If(target <0) return false
if(target==0) return true
for(let num of nums){
var remaining= target-num
if(cansum(remaining, nums)===true){
memo [target]=true
return true
}
}
memo[target]=false
return false
}