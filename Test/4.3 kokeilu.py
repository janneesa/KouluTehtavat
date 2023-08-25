lista = []

while True:
    luvut = input('Anna luku. Tyhjä rivi suorittaa toiminnon: ')

    if luvut == '':
        break #lopettaa toiminnon

    numero = float(luvut)
    lista.append(numero) # lisätään float luku listaan

if lista:
    pienin = min(lista)
    suurin = max(lista)

    print(f'Pienin luku on {pienin:.2f}')
    print(f'suurin luku on {suurin:.2f}')

else:
    print('ei lukuja')
