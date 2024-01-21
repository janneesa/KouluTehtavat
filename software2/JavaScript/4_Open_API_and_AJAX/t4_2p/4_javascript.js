'use strict';

const lomake = document.querySelector('form');
const tulokset = document.querySelector('#tulokset');

lomake.addEventListener('submit', async function(event) {
  event.preventDefault();
  tulokset.innerHTML = '';

  const hakusana = document.querySelector('#query').value;
  console.log(hakusana);

  const vastaus = await fetch(
      `https://api.tvmaze.com/search/shows?q=${hakusana}`);
  const sarjat = await vastaus.json();

  for (const sarja of sarjat) {
    console.log(sarja.show);

    const artikkeli = document.createElement('article');

    const otsikko = document.createElement('h2');
    otsikko.innerText = sarja.show.name;

    const kuva = document.createElement('img');
    kuva.src = sarja.show.image ?
        sarja.show.image.medium :
        'https://placekitten.com/210/295';
    kuva.alt = 'kuva sarjasta';

    const url = document.createElement('a');
    url.href = sarja.show.url;
    url.target = '_blank';
    url.innerText = sarja.show.url;

    const summary = document.createElement('div');
    summary.innerHTML = sarja.show.summary;

    console.log(url.href);

    artikkeli.appendChild(otsikko);
    artikkeli.appendChild(kuva);
    artikkeli.appendChild(url);
    artikkeli.appendChild(summary);
    tulokset.appendChild(artikkeli);
  }
});