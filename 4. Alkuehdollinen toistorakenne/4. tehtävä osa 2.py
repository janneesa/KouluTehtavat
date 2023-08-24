#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
#kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

while True:
    x = float(input('Anna tuumat: '))
    if x < 0:
        print('Et voi antaa negatiivista lukua!')
        break

    y = x * 2.54
    print(str(y) + 'cm')

