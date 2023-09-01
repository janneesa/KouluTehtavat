luku = int(input('Anna luku: '))

if luku == 1:
    print(f'{luku} ei ole alkuluku')

for x in range(2, luku):
    if luku % x == 0:
        print('ei ole')
        break

if luku != 1:
    print('luku on alkuluku')
