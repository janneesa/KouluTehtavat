while True:

    vuosi = int(input('Ilmoita vuosi: '))

    if vuosi % 4 == 0 and vuosi % 100 == 0 and vuosi % 400 != 0 or vuosi % 4:
        print('Vuosi ei ole karkausvuosi')

    else:
        print('Vuosi on karkausvuosi')
