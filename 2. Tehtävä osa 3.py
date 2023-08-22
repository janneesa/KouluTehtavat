kanta = input('Mikä on neliön kannan pituus: ')
korkeus = input('Mikä on neliön korkeus ')

ala = float(kanta) * float(korkeus)
print('Neliön pinta-ala on: ' + str(ala))

piiri = float(kanta) + float(korkeus) * 2
print('Neliön piiri on: ' + str(piiri))