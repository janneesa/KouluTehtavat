'use strict';

async function hae_vitsi() {
  try {
    const vastaus = await fetch(`https://api.chucknorris.io/jokes/random`);

    if (!vastaus.ok) {
      throw new Error(`Virheellinen vastaus: ${vastaus.status}`);
    }

    const value = await vastaus.json();
    console.log(value.value);
    return value.value
  } catch (error) {
    console.error('Virhe pyynnössä:', error.message);
  }
}

hae_vitsi();


