const allConstruct = (target, wordbank, memo = {}) => {
  if (memo[target] in memo) return memo[target]
  if (target === '') return [[]]
  var results = []

  for (let word of wordbank) {
    if (target.indexOf(word) === 0) {
      let suffix = target.slice(word.length)
      const possible = allConstruct(suffix, wordbank, memo)
      const targetWays = possible.map((ways) => [word, ...ways])
      results.push(...targetWays)
    }
  }
  memo[target] = results
  return results
}
console.log(
  allConstruct('abcdef', ['abc', 'ab', 'cd', 'def', 'abcd', 'abcdef'])
)
console.log(
  allConstruct('eeeeeeeeeeeeeeeeeeeeeeef', ['fe', 'feeeef', 'eeeeeeef'])
)
