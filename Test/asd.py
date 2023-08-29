lista = []

while True:
    nimi = input('Anna nimi: ')

    if nimi == '':
        break
    lista.append(nimi)

for nimi in lista:
    print(nimi)
