'use strict';

function operation(){

  const input1 = document.getElementById('calculation').value
  const p_element = document.getElementById('result')

  if (input1.includes('+')){
    const [num1, num2] = input1.split('+')
    p_element.innerText = parseInt(num1) + parseInt(num2);
  }

  if (input1.includes('-')){
    const [num1, num2] = input1.split('-')
    p_element.innerText = parseInt(num1) - parseInt(num2);
  }

  if (input1.includes('*')){
    const [num1, num2] = input1.split('*')
    p_element.innerText = parseInt(num1) * parseInt(num2);
  }

  if (input1.includes('/')){
    const [num1, num2] = input1.split('/')
    p_element.innerText = parseInt(num1) / parseInt(num2);
  }

}