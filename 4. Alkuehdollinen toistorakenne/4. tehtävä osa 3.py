pienin = float('inf')
suurin = float('-inf')

y = 0

while y < 1:
    x = input('Anna luku: (tyhjä rivi lopettaa): ')

    if x == '':
        y += 1
        break

    luku = float(x)

    if luku < pienin:
        pienin = luku

    if luku > suurin:
        suurin = luku

print(f'pienin luku on: {pienin} ja suurin luku on: {suurin}')
