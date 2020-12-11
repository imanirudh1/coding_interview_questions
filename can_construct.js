const can_construct = (target, wordbank, memo = {}) => {
  if (memo[target] in memo) return memo[target]
  if (target === '') return true
  for (let word of wordbank) {
    if (target.indexOf(word) === 0) {
      let suffix = target.slice(word.length)
      if (can_construct(suffix, wordbank, memo)) {
        memo[target] = true
        return true
      }
    }
  }
  memo[target] = false
  return false
}

console.log(can_construct('abcdef', ['abc', 'ab', 'cd', 'def', 'abcd']))
console.log(
  can_construct('eeeeeeeeeeeeeeeeeeeeeeef', ['fe', 'feeeef', 'eeeeeeef'])
)
