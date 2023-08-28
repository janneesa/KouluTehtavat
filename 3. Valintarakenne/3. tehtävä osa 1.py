kuha = float(input('Mikä on kuhan pituus senttimetreinä: '))
print('Kuhan pituus: ' + str(kuha) + 'cm')

mitta = 37

haluttu = mitta - kuha

if kuha < mitta:
    print('Kuha on alimittainen. pituudesta puuttuu: ' + str(haluttu) + 'cm. Laske se takaisin järveen')
else: print('Onneksi olkoon! Kuha hyväksytyn pituinen.')