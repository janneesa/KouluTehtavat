import random

luku = random.randint(1, 100)

arvaus = int(input('Arvaa mitä lukua ajattelen 1-100: '))

while arvaus != luku:
    if arvaus < luku:
        print('Liian pieni arvaus.')
        arvaus = int(input('Arvaa uudestaan :) '))

    if arvaus > luku:
        print('Liian suuri arvaus.')
        arvaus = int(input('Arvaa uudestaan :) '))

    else:
        print('Oikein! Voitit pelin!')
        break
