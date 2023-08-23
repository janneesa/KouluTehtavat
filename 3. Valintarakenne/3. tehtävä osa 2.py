luokka = input('Mikä on hyttiluokkasi:LUX, A, B, C: ')

if luokka == 'LUX' or luokka == 'lux':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif luokka == 'A' or luokka == 'a':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif luokka == 'B' or luokka == 'b':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif luokka == 'C' or luokka == 'c' :
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka')
