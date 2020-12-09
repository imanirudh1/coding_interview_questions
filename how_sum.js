const how_sum = (target, nums, memo = {}) => {
  if (memo[target] in memo) return memo[target]
  if (target === 0) return []
  if (target < 0) return null
  for (let num of nums) {
    var remaining = target - num
    var remainingResult = how_sum(remaining, nums, memo)
    if (remainingResult != null) {
      memo[target] = [...remainingResult, num]
      return memo[target]
    }
  }
  memo[target] = null
  return memo[target]
}
console.log(how_sum(7, [2, 3]))
