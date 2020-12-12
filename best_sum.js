// const best_sum = (target, nums, memo = {}) => {
//   if (memo[target] in memo) return memo[target]
//   if (target === 0) return []
//   if (target < 0) return null
//   var shortestCombination = null
//   for (let num of nums) {
//     var remainder = target - num
//     var remainderCombination = best_sum(remainder, nums, memo)
//     if (remainderCombination != null) {
//       var combination = [...remainderCombination, num]
//       if (
//         shortestCombination === null ||
//         combination.length < shortestCombination.length
//       ) {
//         shortestCombination = combination
//       }
//     }
//   }
//   memo[target] = shortestCombination
//   return memo[target]
// }

const best_sum = (target, nums) => {
  const table = Array(target + 1).fill(null)
  table[0] = []
  for (let i = 0; i <= target; i++) {
    if (table[i] != null) {
      for (let num of nums) {
        if (num + i <= target) {
          let arr = [...table[i], num]
          if (table[i + num] === null) {
            table[i + num] = arr
          } else if (table[i + num] && arr.length < table[i + num].length) {
            table[i + num] = arr
          }
        }
      }
    }
  }
  return table[target]
}

console.log(best_sum(100, [1, 2, 3, 5, 25]))
