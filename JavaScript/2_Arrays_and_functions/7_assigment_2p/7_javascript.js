function dice_roll(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

let rolls = []

let roll = null

const sides = parseInt(prompt('How many sides?'));

while (roll !== sides) {
  roll = dice_roll(sides);
  rolls.push(`<li>${roll}</li>`);
}

const rollsHTML = '<ul>' + rolls.join('') + '</ul>';

document.querySelector('#target').innerHTML = rollsHTML;