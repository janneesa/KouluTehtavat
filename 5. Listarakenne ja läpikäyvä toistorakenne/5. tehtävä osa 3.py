luku = int(input('Anna luku: '))

ei = False

if luku == 1:
    print(f'{luku} Ei ole alkuluku')

for x in range(2, luku):
    if luku % x == 0:
        print('Ei ole alkuluku')
        ei = True
        break

if ei == False and luku != 1:
    print('On alkuluku')


