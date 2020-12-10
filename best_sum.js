const best_sum = (target, nums, memo = {}) => {
  if (memo[target] in memo) return memo[target]
  if (target === 0) return []
  if (target < 0) return null
  var shortestCombination = null
  for (let num of nums) {
    var remainder = target - num
    var remainderCombination = best_sum(remainder, nums, memo)
    if (remainderCombination != null) {
      var combination = [...remainderCombination, num]
      if (
        shortestCombination === null ||
        combination.length < shortestCombination.length
      ) {
        shortestCombination = combination
      }
    }
  }
  memo[target] = shortestCombination
  return memo[target]
}

console.log(best_sum(100, [34, 36, 2, 25]))
