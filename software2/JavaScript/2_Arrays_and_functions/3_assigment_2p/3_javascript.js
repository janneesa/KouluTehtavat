let names = [];

for (let dog_nmb = 0; dog_nmb < 6; dog_nmb++) {
  const dog_name = prompt(`What is ${dog_nmb + 1}. dogs name?`);
  names.push(`<li>${dog_name}</li>`);
}

names.sort()
names.reverse();

const namesHTML = '<ul>' + names.join('') + '</ul>';

document.querySelector('#target').innerHTML = namesHTML;
