const name = prompt('Type your name.')
const house = Math.floor(Math.random() * 4) + 1;
if (house === 1) {
  document.querySelector('#target').innerHTML = name + ', you are Gryffindor';
} else if (house === 2) {
  document.querySelector('#target').innerHTML = name + ', you are Slytherin';
} else if (house === 3) {
  document.querySelector('#target').innerHTML = name + ', you are Hufflepuff';
} else if (house === 4) {
  document.querySelector('#target').innerHTML = name + ', you are Ravenclaw';
}
