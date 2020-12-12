// const cansum = (target, nums, memo = {}) => {
//   if (target in memo) return memo[target]
//   if (target < 0) return false
//   if (target === 0) return true
//   for (let num of nums) {
//     var remaining = target - num
//     if (cansum(remaining, nums) === true) {
//       memo[target] = true
//       return true
//     }
//   }
//   memo[target] = false
//   return false
// }

const cansum = (target, nums) => {
  const table = Array(target + 1).fill(false)
  table[0] = true
  for (let i = 0; i <= target; i++) {
    if (table[i] == true) {
      for (let num of nums) {
        table[i + num] = true
      }
    }
  }
  return table[target]
}

console.log(cansum(7, [2, 3]))
