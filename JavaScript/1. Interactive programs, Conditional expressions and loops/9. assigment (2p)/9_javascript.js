const number = parseInt(prompt('Input a number.'));

let isPrime = true;

if (number === 1) {
    isPrime = false;
} else if (number > 1) {
    for (let i = 2; i < number; i++) {
        if (number % i === 0) {
            isPrime = false;
            break;
        }
    }
}

if (isPrime) {
    document.querySelector('#target').innerHTML = `${number} is a prime number.`;
} else {
    document.querySelector('#target').innerHTML = `${number} is not a prime number.`;
}


