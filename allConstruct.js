// const allConstruct = (target, wordbank, memo = {}) => {
//   if (memo[target] in memo) return memo[target]
//   if (target === '') return [[]]
//   var results = []

//   for (let word of wordbank) {
//     if (target.indexOf(word) === 0) {
//       let suffix = target.slice(word.length)
//       const possible = allConstruct(suffix, wordbank, memo)
//       const targetWays = possible.map((ways) => [word, ...ways])
//       results.push(...targetWays)
//     }
//   }
//   memo[target] = results
//   return results
// }

const allConstruct = (target, wordbank) => {
  const table = Array(target.length + 1)
    .fill()
    .map(() => [])
  table[0] = [[]]
  for (let i = 0; i <= target.length; i++) {
    if (table[i].length > 0) {
      for (let word of wordbank) {
        if (target.slice(i, i + word.length) === word) {
          table[i + word.length].push(
            ...table[i].map((item) => [...item, word])
          )
        }
      }
    }
  }
  return table[target.length]
}

console.log(
  allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])
)
console.log(
  allConstruct('eeeeeeeeeeeeeeeeeeeeeeef', ['fe', 'feeeef', 'eeeeeeef'])
)
