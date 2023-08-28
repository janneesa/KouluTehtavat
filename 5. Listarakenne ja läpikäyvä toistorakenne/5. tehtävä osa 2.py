numerot = [] #luodaan tyhjä lista

luku = (input('Syötä luku: (Tyhjä rivi lopettaa): '))
numerot.append(luku)

while luku != '':
    luku = (input('Syötä lisää lukuja: (Tyhjä rivi lopettaa): '))
    numerot.append(luku)

    if luku == '':
        numerot.sort(reverse=True)
        print(luku[:5])
        break


