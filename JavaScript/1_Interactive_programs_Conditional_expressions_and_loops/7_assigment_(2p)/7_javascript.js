const number = parseInt(prompt('How many dice do you want to throw?'))
let sum = 0
for (let i = 1; i <= number; i++) {
  let dice = Math.floor(Math.random() * 6) + 1
  sum += + dice
  console.log(dice, sum)
}
document.querySelector('#target').innerHTML = `Sum is: ${sum}`;
