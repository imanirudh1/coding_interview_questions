const count_construct = (target, wordbank, memo = {}) => {
  if (memo[target] in memo) return memo[target]
  if (target === '') return 1
  var count = 0
  for (let word of wordbank) {
    if (target.indexOf(word) === 0) {
      let suffix = target.slice(word.length)
      const numOfWays = count_construct(suffix, wordbank, memo)
      count += numOfWays
    }
  }
  memo[target] = count
  return count
}
console.log(
  count_construct('abcdef', ['abc', 'ab', 'cd', 'def', 'abcd', 'abcdef'])
)
console.log(
  count_construct('eeeeeeeeeeeeeeeeeeeeeeef', ['fe', 'feeeef', 'eeeeeeef'])
)
