pienin = None
suurin = None

while True:
    luku = input('Anna lukuja: (tyhjä rivi tulostaa pienimmän ja suurimman luvun): ')

    if luku == '':
        print(f'suurin luku on {suurin} ja pienin luku on {pienin}.')
        break

    x = float(luku)

    if pienin is None or x < pienin:
        pienin = x

    if suurin is None or x > suurin:
        suurin = x
