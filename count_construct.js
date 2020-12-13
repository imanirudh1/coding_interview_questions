// const count_construct = (target, wordbank, memo = {}) => {
//   if (memo[target] in memo) return memo[target]
//   if (target === '') return 1
//   var count = 0
//   for (let word of wordbank) {
//     if (target.indexOf(word) === 0) {
//       let suffix = target.slice(word.length)
//       const numOfWays = count_construct(suffix, wordbank, memo)
//       count += numOfWays
//     }
//   }
//   memo[target] = count
//   return count
// }
const count_construct = (target, wordbank) => {
  const table = Array(target.length + 1).fill(0)
  table[0] = 1
  for (let i = 0; i <= target.length; i++) {
    if (table[i] > 0) {
      for (let word of wordbank) {
        if (target.slice(i, i + word.length) === word) {
          table[i + word.length] += table[i]
        }
      }
    }
  }
  return table[target.length]
}

console.log(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
console.log(
  count_construct('eeeeeeeeeeeeeeeeeeeeeeef', ['fe', 'feeeef', 'eeeeeeef'])
)
