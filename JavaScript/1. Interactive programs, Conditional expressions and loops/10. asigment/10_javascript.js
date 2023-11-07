const number_of_dice = parseInt(prompt('How many dice?'));
const sum = parseInt(prompt('Target sum?'));

let target = 0;

for (let i = 0; i < 10000; i++) {
  let current_sum = 0;
  for (let a = 0; a < number_of_dice; a++) {
    let dice = Math.floor(Math.random() * 6) + 1;
    current_sum += dice;
  }
  if (current_sum === sum) {
    target++;
  }
}

let probability = (target / 10000) * 100;

document.querySelector('#target').innerHTML = `Probability to get sum ${sum} with ${number_of_dice} dice is ${probability}%`;
