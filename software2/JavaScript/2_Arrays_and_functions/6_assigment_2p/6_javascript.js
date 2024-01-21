function dice_roll() {
  return Math.floor(Math.random() * 6) + 1;
}

let rolls = []

let roll = null

while (roll !== 6) {
  roll = dice_roll();
  rolls.push(`<li>${roll}</li>`);
}

const rollsHTML = '<ul>' + rolls.join('') + '</ul>';

document.querySelector('#target').innerHTML = rollsHTML;