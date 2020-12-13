// const can_construct = (target, wordbank, memo = {}) => {
//   if (memo[target] in memo) return memo[target]
//   if (target === '') return true
//   for (let word of wordbank) {
//     if (target.indexOf(word) === 0) {
//       let suffix = target.slice(word.length)
//       if (can_construct(suffix, wordbank, memo)) {
//         memo[target] = true
//         return true
//       }
//     }
//   }
//   memo[target] = false
//   return false
// }

const can_construct = (target, wordbank) => {
  const table = Array(target.length + 1).fill(false)
  table[0] = true
  for (let i = 0; i <= target.length; i++) {
    if (table[i] === true) {
      for (let word of wordbank) {
        if (target.slice(i, i + word.length) === word) {
          table[i + word.length] = true
        }
      }
    }
  }
  return table[target.length]
}

console.log(can_construct('abcdef', ['abc', 'ab', 'cd', 'def', 'abcd']))
console.log(
  can_construct('eeeeeeeeeeeeeeeeeeeeeeef', ['fe', 'feeeef', 'eeeeeeef'])
)
