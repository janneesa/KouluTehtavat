const answer = confirm('Should I calculate the square root?')

if (answer === true) {
  const number = parseInt(prompt('Input a positive number.'))

  if (number <= 0) {
    document.querySelector('#target').innerHTML = 'The square root of a negative number or zero is not defined';
  }

  else {
    document.querySelector('#target_2').innerHTML = `The square root of ${number} is: ` + Math.sqrt(number);
  }
}

else {
  document.querySelector('#target_3').innerHTML = 'The square root is not calculated.';
}