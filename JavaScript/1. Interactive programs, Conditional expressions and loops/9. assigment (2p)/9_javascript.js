const number = parseInt(prompt('Input a number.'))
for (let i = 2; number; i++ ) {
    if (number % i === 0) {
        document.querySelector('#target').innerHTML = `${number} is not a prime number.`;
        console.log(i)
        break
    }
}

