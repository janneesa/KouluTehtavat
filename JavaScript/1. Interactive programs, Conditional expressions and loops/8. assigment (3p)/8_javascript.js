const start_year = parseInt(prompt('Input a starting year.'))
const end_year = parseInt(prompt('Input an ending year.'))

let leapyears = ''

for (let i = start_year; i <= end_year; i++) {
  if (i % 400 === 0 || i % 100 !== 0 && i % 4 === 0) {
    leapyears += '<li>' + i + '</li>';
  }
}

document.querySelector('#target').innerHTML = leapyears;