luokka = input('Mikä on hyttiluokkasi: LUX, A, B, C: ')

if luokka.upper() == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif luokka.upper() == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif luokka.upper() == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif luokka.upper() == 'C':
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka')
