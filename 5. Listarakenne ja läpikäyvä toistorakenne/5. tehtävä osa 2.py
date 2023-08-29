#todo tee tästä simppelimpi
#todo tyhjän rivin täytyy lopettaa toiminto

numerot = []  #luodaan tyhjä lista

luku = (input('Syötä luku: (Tyhjä rivi lopettaa): '))
while luku == '':
    luku = input('Syötä lisää lukuja: ')

luku_int = int(luku)
numerot.append(luku_int)  #lisätään luku listaan

while luku != '':
    luku = (input('Syötä lisää lukuja: (Tyhjä rivi lopettaa): '))

    if luku == '':
        break  #sammutetaan loop

    luku_int = int(luku)
    numerot.append(luku_int)  #loopataan toiminta

numerot.sort(reverse=True)  #sorttaa listan käänteisessä järjestyksessä

print(numerot[:5])  #printtaa 5 ekaa käänteisessä eli suurimmasta pienimpään järkässä
