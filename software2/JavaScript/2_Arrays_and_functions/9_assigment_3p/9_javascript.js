const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



function even(numbers) {

  let even_numbers = []

  for (let i = 0; i < numbers.length; i++){

    if (numbers[i] % 2 === 0){
      even_numbers.push(numbers[i])
    }
  }
  return even_numbers
}

console.log(numbers)
console.log(even(numbers))