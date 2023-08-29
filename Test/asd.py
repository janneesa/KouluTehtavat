vuosi = int(input('Anna vuosiluku: '))

if vuosi % 400 == 0 and vuosi % 100 == 0 or vuosi % 4 == 0 and vuosi % 100 != 0:
    print('karkausvuosi')
else:
    print('Ei ole karkausvuosi')


if vuosi % 4 == 0 and vuosi % 100 != 0:
    print('karkausvuosi')
elif vuosi % 400 == 0 and vuosi % 100 == 0:
    print('karkausvuosi')
else:
    print('ei ole')

