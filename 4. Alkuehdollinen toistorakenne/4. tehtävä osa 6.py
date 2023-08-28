#todo tee uusi versio

import random

arvottavien_pisteiden_maara = int(input("Syötä arvottavien pisteiden määrä: "))
ympyran_sisalla = 0

for _ in range(arvottavien_pisteiden_maara):
    x = random.uniform(-1, 1)  # Arvotaan satunnainen x-koordinaatti
    y = random.uniform(-1, 1)  # Arvotaan satunnainen y-koordinaatti

    if x ** 2 + y ** 2 < 1:  # Tarkistetaan, onko piste ympyrän sisällä
        ympyran_sisalla += 1

piin_likiarvo = 4 * ympyran_sisalla / arvottavien_pisteiden_maara
print(f"Laskettu piin likiarvo: {piin_likiarvo:.6f}")

