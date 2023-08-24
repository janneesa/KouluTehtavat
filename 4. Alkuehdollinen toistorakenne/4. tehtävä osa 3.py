import random

x = random.randint(1, 10)
print(x)
arvaus = int(input('Mitä lukua ajattelen 1-10: '))

while True:
    if arvaus < x:
        print('liian vähän')
        arvaus = int(input('arvaa uudestaan: '))
    elif arvaus > x:
        print('liian paljon')
        arvaus = int(input('arvaa uudestaan: '))
    elif arvaus == x:
        print('voitit pelin')
        break




