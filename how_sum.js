// const how_sum = (target, nums, memo = {}) => {
//   if (memo[target] in memo) return memo[target]
//   if (target === 0) return []
//   if (target < 0) return null
//   for (let num of nums) {
//     var remaining = target - num
//     var remainingResult = how_sum(remaining, nums, memo)
//     if (remainingResult != null) {
//       memo[target] = [...remainingResult, num]
//       return memo[target]
//     }
//   }
//   memo[target] = null
//   return memo[target]
// }

const how_sum = (target, nums) => {
  const table = Array(target + 1).fill(null)
  table[0] = []
  for (let i = 0; i <= target; i++) {
    if (table[i] != null) {
      for (let num of nums) {
        if (num + i <= target) table[i + num] = [...table[i], num]
        if (table[target]) return table[target]
      }
    }
  }
  return table[target]
}

console.log(how_sum(7, [5, 3, 4]))
