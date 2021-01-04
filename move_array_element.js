const arr = [1, 2, 3, 4, 5]

function moveEle(arr, index, offset) {
  var position = index + offset
  if (position < arr.length && position >= 0) {
    var output = [...arr]
    var element = output.splice(index, 1)[0]
    output.splice(position, 0, element)
    return output
  } else {
    console.error('Invalid')
  }
}
console.log(moveEle(arr, 1, -1))
