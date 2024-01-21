const participants = parseInt(prompt('How many participants?'));

let names = [];

for (let i = 0; i < participants; i++) {
  let name = prompt(`Write ${i + 1}. participant's name.`);
  names.push(`<li>${name}</li>`);
}

names.sort();

const namesHTML = '<ol>' + names.join('') + '</ol>';

document.querySelector('#target').innerHTML = namesHTML;
