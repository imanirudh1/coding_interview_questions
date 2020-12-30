//Ques 1
let num
for (var i = 0; i < 5; i++) {
  num = i
  setTimeout(function () {
    console.log(num)
  }, 1000)
}
