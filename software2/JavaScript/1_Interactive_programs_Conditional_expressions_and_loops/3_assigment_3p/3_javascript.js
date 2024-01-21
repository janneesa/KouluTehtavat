const number1 = parseInt(prompt('Give first number.'))
const number2 = parseInt(prompt('Give second number.'))
const number3 = parseInt(prompt('Give third number.'))

const sum = number1 + number2 + number3
const product = number1 * number2 * number3
const average = (number1 + number2 + number3) / 3

document.querySelector('#target_1').innerHTML = 'Sum: ' + sum;
document.querySelector('#target_2').innerHTML = 'Product: ' + product;
document.querySelector('#target_3').innerHTML = 'Average: ' + average;