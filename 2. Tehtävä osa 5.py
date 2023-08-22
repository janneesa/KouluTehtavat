Leiviska = float(input('Montako leiviskää: '))
Naula = float(input('Montako naulaa: '))
Luoti = float(input('Montako luotia: '))

kokonais_summa = (Leiviska * 20 * 32 * 13.3) + (Naula * 32 * 13.3) + (Luoti * 13.3)
kiloina = kokonais_summa / 1000

kokonais_kg = int(kiloina)

grammat = (kiloina - kokonais_kg) * 1000

print('Massa nykyaikaisilla mitoilla: ')
print(f'{kokonais_kg}kg ja  {grammat:.0f}grammaa')


