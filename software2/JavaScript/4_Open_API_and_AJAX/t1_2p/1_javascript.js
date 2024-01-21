'use strict';

const lomake = document.querySelector('form');

lomake.addEventListener('submit', async function(event){
  event.preventDefault();
  const vastaus = await fetch('https://api.tvmaze.com/search/shows?q=friends');
  const data = await vastaus.json();
  console.log(data);
});