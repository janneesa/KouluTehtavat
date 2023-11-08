let numbers = []

let number

while (true) {
  number = parseInt(prompt('Write a number.'))
  if (numbers.includes(number)){
    break
  }
  numbers.push(number)
}

numbers.sort((a, b) => a - b);

console.log(numbers);