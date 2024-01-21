function concat(array) {
  let string = ''
  for (let i = 0; i < array.length; i++){
    string += array[i]
  }
  return string
}

const names = ['Johnny', 'DeeDee', 'Joey', 'Marky']

concat(names)

document.querySelector('#target').innerHTML = concat(names);