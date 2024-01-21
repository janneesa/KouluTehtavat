'use strict';

const lomake = document.querySelector('form');

lomake.addEventListener('submit', async function(event){
  event.preventDefault();
  const hakusana = document.querySelector('#query').value;
  console.log(hakusana)
  const vastaus = await fetch(`https://api.tvmaze.com/search/shows?q=${hakusana}`);
  const data = await vastaus.json();
  console.log(data);
});