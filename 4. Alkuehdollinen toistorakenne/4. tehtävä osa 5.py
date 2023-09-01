x = "python"
y = 'rules'

i = 5

x1 = input('Anna käyttäjätunnus: ')
y1 = input('Anna salasana: ')


while i > 0:
    if i == 1:
        print('Pääsy evätty')
        break

    if x1 != x or y1 != y:
        print('väärin')
        i = i - 1
        x1 = input('Anna käyttäjätunnus: ')
        y1 = input('Anna salasana: ')

    if x1 == x and y1 == y:
        print('Tervetuloa')
        break

if i < 1:
    print('Pääsy evätty')
