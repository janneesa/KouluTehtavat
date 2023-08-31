nimet = set()

while True:
    nimi = input('Anna nimi: (tyhjä rivi suorittaa toiminnon): ')
    if nimi == '':
        break
    if nimi in nimet:
        print('Aiemmin syötetty nimi.')
    else:
        nimet.add(nimi)
        print('Uusi nimi.')
for x in nimet:
    print(x)
