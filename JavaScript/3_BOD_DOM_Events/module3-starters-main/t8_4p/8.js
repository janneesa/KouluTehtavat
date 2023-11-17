'use strict';

function operation(){

  const input1 = document.getElementById('num1').value
  const input2 = document.getElementById('num2').value
  const p_element = document.getElementById('result')

  const calc_option = document.getElementById('operation').value

  switch (calc_option){
    case 'add':
      p_element.innerText = parseInt(input1) + parseInt(input2);
      break

    case 'sub':
      p_element.innerText = parseInt(input1) - parseInt(input2);
      break

    case 'multi':
      p_element.innerText = parseInt(input1) * parseInt(input2);
      break

    case 'div':
      p_element.innerText = parseInt(input1) / parseInt(input2);
      break
  }

}

