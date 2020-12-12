// const grid_traversal = (m, n, memo = {}) => {
//   let key = m + ',' + n
//   if (key in memo) return memo[key]
//   if (m === 0 || n === 0) return 0
//   if (m === 1 && n === 1) return 1
//   memo[key] = grid_traversal(m - 1, n, memo) + grid_traversal(m, n - 1, memo)
//   return memo[key]
// }

const grid_traversal = (m, n) => {
  const table = Array(m + 1)
    .fill()
    .map(() => Array(n + 1).fill(0))
  table[1][1] = 1
  for (let i = 0; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      const current = table[i][j]
      if (i < m) table[i + 1][j] += current
      if (j < n) table[i][j + 1] += current
    }
  }
  return table[m][n]
}

console.log(grid_traversal(18, 18))
