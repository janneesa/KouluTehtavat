'use strickt';

const text = document.querySelector('#trigger');
const pic = document.querySelector('#target');

text.addEventListener('mouseover', function(){
  pic.src = 'img/picB.jpg'
})

text.addEventListener('mouseout', function(){
  pic.src = 'img/picA.jpg'
})
