const arr = [1, 23, 4, 5, 54, 44, 1]
function countOccurance(arr, searchEle) {
  return arr.reduce((acc, cur) => {
    const occurance = searchEle === cur ? 1 : 0
    return acc + occurance
  }, 0)
}

console.log(countOccurance(arr, 1))
