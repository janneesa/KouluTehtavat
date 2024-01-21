import random

x = random.randint(1, 10)

arvaus = int(input('Mitä lukua ajattelen 1-10: '))

while True:
    if arvaus < x:
        print('liian pieni arvaus')
        arvaus = int(input('arvaa uudestaan: '))
    elif arvaus > x:
        print('liian suuri arvaus')
        arvaus = int(input('arvaa uudestaan: '))
    elif arvaus == x:
        print('Oikein!')
        break
