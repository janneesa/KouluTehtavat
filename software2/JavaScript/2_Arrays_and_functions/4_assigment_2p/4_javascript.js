let numbers = []

let number = null

while (number !== 0) {
  number = parseInt(prompt('Write a number. Type 0 to stop.'))
  if (number === 0){
    break
  }
  numbers.push(number)
}

numbers.sort((a, b) => b - a);

console.log(numbers);