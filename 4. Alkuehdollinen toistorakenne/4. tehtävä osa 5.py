x = "python"
y = 'rules'

i = 4

x1 = input('Anna käyttäjätunnus: ')
y1 = input('Anna salasana: ')


while i>0:
    if x1 == x and y1 == y:
        print('oikein')
        break
    if x1 != x or y1 != y:
        print('väärin')
        i = i -1
        x1 = input('Anna käyttäjätunnus: ')
        y1 = input('Anna salasana: ')
    if i<=0 :
        print('pääsy evätty')
        break












