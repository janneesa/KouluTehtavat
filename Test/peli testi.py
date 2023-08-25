import random

x = random.randint(1, 10)

arvaus = int(input('Mitä lukua ajattelen 1-10: '))

maara = 1
while True:
    if arvaus < x:
        print('liian pieni arvaus')
        arvaus = int(input('arvaa uudestaan: '))
        maara = maara + 1
    elif arvaus > x:
        print('liian suuri arvaus')
        arvaus = int(input('arvaa uudestaan: '))
        maara = maara + 1
    elif arvaus == x:
        print('Oikein! Arvauksia oli ' + str(maara) + 'kpl')
        break
