var row = 4
var col = 5

var matrix = Array(row)
  .fill([])
  .map(() => Array(col).fill(0))

for (let i = 0; i < row; i++) {
  for (let j = 0; j < col; j++) {
    if (j === 0) {
      matrix[i][j] = i + 1
    } else if (i === 0) {
      if (j % 2 === 0) {
        matrix[i][j] = row * j + 1
      } else {
        matrix[i][j] = row * (j + 1)
      }
    } else {
      if (j % 2 === 0) {
        matrix[i][j] = matrix[i - 1][j] + 1
      } else {
        matrix[i][j] = matrix[i - 1][j] - 1
      }
    }
  }
}
console.log(matrix)
