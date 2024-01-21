'use strict';

const lomake = document.querySelector('form');

const article = document.querySelector('article');

lomake.addEventListener('submit', async function(event) {
  event.preventDefault();

  article.innerText = '';

  const hakusana = document.querySelector('#query').value;
  console.log(hakusana);

  const vastaus = await fetch(
      `https://api.chucknorris.io/jokes/search?query=${hakusana}`);
  const data = await vastaus.json();
  console.log(data);

  for (const vitsi of data.result) {
    const joke = document.createElement('p');
    joke.innerText = vitsi.value;
    article.appendChild(joke);
  }

});


